from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import bezier
import numpy as np
import pdb


def plot_ttf(letter):
    with open("cambam5.ttx") as f:
        soup = BeautifulSoup(f, "xml")

    ax = plt.axes()

    soup = soup.find("glyf")
    glyph = soup.find("TTGlyph", attrs={"name": letter})

    for contour in glyph.find_all("contour"):
        pts = contour.find_all("pt")
        x = np.array([int(pt["x"]) for pt in pts], dtype=np.double)
        y = np.array([int(pt["y"]) for pt in pts], dtype=np.double)

        for i in range(0, len(x), 2):
            x_slice = x.take(range(i - 1, i + 2), mode="wrap")
            y_slice = y.take(range(i - 1, i + 2), mode="wrap")
            curve = bezier.Curve(np.asfortranarray([x_slice, y_slice]), degree=3)
            curve.plot(num_pts=256, ax=ax)

    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    plot_ttf("A")
