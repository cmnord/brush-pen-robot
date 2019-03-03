import bezier
from bs4 import BeautifulSoup, element
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple


class Glyph:
    def __init__(self, soup: element.Tag, name: str, width: int, height: int):
        self.soup = soup
        self.name = name
        self.width = width
        self.height = height
        self.contours = []
        for contour in self.soup.find_all("contour"):
            pts = contour.find_all("pt")
            x = np.array([int(pt["x"]) for pt in pts], dtype=np.double)
            y = np.array([int(pt["y"]) for pt in pts], dtype=np.double)
            on = np.array([pt["on"] == "1" for pt in pts], dtype=np.bool)
            self.contours.append((x, y, on))

    def interpolate_path(self, resolution: int) -> np.ndarray:
        """ Interpolate points to the given resolution for each contour in this glyph."""
        all_points = np.ndarray((2, 0))
        curves = self.get_curves()
        for curve in curves:
            # TODO: base num on curve.length()?
            x = np.linspace(0, 1, num=resolution)
            points = curve.evaluate_multi(x)
            all_points = np.concatenate((all_points, points), 1)
        return all_points

    def get_gcode(self, base_x: int, base_y: int, resolution: int) -> str:
        """ Return a string of GCode to print this glyph starting from the relative base x and y indices."""
        path = self.interpolate_path(resolution)
        out = ""
        for x, y in path.T:
            x_relative = int(base_x + x)
            y_relative = int(base_y + y)
            out += "G1 X{} Y{} Z{};\n".format(x_relative, y_relative, self.width)
        return out

    def plot(self):
        """ Plot this glyph on its own graph."""
        ax = plt.axes()

        for x, y, on in self.contours:
            assert len(x) == len(y) == len(on)
            curve_start = 0
            curve_end = 1
            print(on)
            plt.scatter(x, y)
            while curve_end < len(on):
                while curve_end < len(on) and not on[curve_end]:
                    curve_end += 1
                curve_end = min(len(on) - 1, curve_end + 1)
                print(curve_start, curve_end)
                degree = curve_end - curve_start - 1
                curve = bezier.Curve(
                    np.asfortranarray(
                        [x[curve_start:curve_end], y[curve_start:curve_end]]
                    ),
                    degree=degree,
                )
                curve.plot(num_pts=256, ax=ax)
                curve_start = curve_end - 1
                curve_end += 1

        # Include height/width dot
        plt.scatter([self.width], [self.height])
        plt.axis("equal")
        plt.show()

    @staticmethod
    def from_font(font_filename: str, name: str) -> "Glyph":
        with open(font_filename) as f:
            soup = BeautifulSoup(f, "xml")
        attrs = {"name": name}
        glyph_soup = soup.find("glyf").find("TTGlyph", attrs=attrs)
        width = int(soup.find("hmtx").find("mtx", attrs=attrs)["width"])
        height = int(soup.find("OS_2").find("sCapHeight")["value"])
        return Glyph(glyph_soup, name, width, height)

