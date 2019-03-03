from font import Font
from glyph import Glyph

FONT = "fonts/cambam5.ttx"
RESOLUTION = 10


def plot_letter(letter, interpolated: bool = False):
    glyph = Glyph.from_font(FONT, letter)
    if interpolated:
        return glyph.plot_interpolated(RESOLUTION)
    return glyph.plot()


def plot_font(interpolated: bool = False):
    font = Font(FONT)
    if interpolated:
        return font.plot_interpolated(RESOLUTION)
    return font.plot()


if __name__ == "__main__":
    letter = "B"
    plot_letter(letter, interpolated=True)
