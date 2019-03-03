import bezier
from bs4 import BeautifulSoup, element
import matplotlib.pyplot as plt
import numpy as np


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
            self.contours.append((x, y))

    def interpolate_path(self, resolution: int):
        """ Interpolate points to the given resolution for each contour in this glyph."""
        return self.contours

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
        for x, y in self.contours:
            for i in range(0, len(x), 2):
                x_slice = x.take(range(i - 1, i + 2), mode="wrap")
                y_slice = y.take(range(i - 1, i + 2), mode="wrap")
                curve = bezier.Curve(np.asfortranarray([x_slice, y_slice]), degree=3)
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

