from font import Font
from glyph import Glyph

FONT = "fonts/cambam5.ttx"


def plot_letter(letter):
    letter = Glyph.from_font(FONT, letter)
    letter.plot()


def plot_font():
    font = Font(FONT)
    font.plot()


if __name__ == "__main__":
    plot_letter("Y")
