import bezier
from bs4 import BeautifulSoup, element
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple


class Glyph:
    SCALE = 0.01
    # TODO: fill in
    Z_LOW = -1
    Z_HIGH = -1

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
            x = np.linspace(0, 1, num=resolution + 1)[:-1]
            points = curve.evaluate_multi(x)
            all_points = np.concatenate((all_points, points), 1)
        return all_points

    def get_gcode(self, base_x: int, base_y: int, resolution: int) -> str:
        """ Return a string of GCode to print this glyph starting from the relative base x and y indices."""
        path = self.interpolate_path(resolution)
        if len(path) == 0:
            return ""
        out = ""
        for x, y in reversed(path.T):
            x_relative = int(base_x + x)
            y_relative = int(base_y + y)
            out += "G1 X{} Y{} F100\n".format(
                x_relative * self.SCALE, y_relative * self.SCALE
            )
        return out

    def get_curves(self) -> List[bezier.Curve]:
        """ Get all the Bezier curves in each contour."""
        curves = []
        if len(self.contours) == 0:
            return curves
        for contour in self.contours:
            num_pts = np.shape(contour)[1]
            half = num_pts // 2 + 1
            num_pts = half
            curve_start = 0
            curve_end = 1
            while curve_end < num_pts:
                while curve_end < num_pts and not contour[2][curve_end]:
                    curve_end += 1
                curve_end = min(num_pts - 1, curve_end + 1)
                degree = curve_end - curve_start - 1
                curve = bezier.Curve(
                    np.asfortranarray(
                        [
                            contour[0][curve_start:curve_end],
                            contour[1][curve_start:curve_end],
                        ]
                    ),
                    degree=degree,
                )
                curves.append(curve)
                curve_start = curve_end - 1
                curve_end += 1
        return curves

    def plot_interpolated(self, resolution: int = 10):
        path = self.interpolate_path(resolution)
        xs = []
        ys = []
        for x, y in path.T:
            xs.append(x)
            ys.append(y)
        plt.scatter(path[0], path[1], alpha=0.3)
        plt.show()

    def plot(self):
        """ Plot this glyph on its own graph."""
        ax = plt.axes()

        curves = self.get_curves()
        for curve in curves:
            curve.plot(num_pts=256, ax=ax)

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

