from font import Font
from glyph import Glyph
import argparse

FONT = "fonts/cambam5.ttx"


def plot_letter(letter: str, interpolated: bool, resolution: int):
    glyph = Glyph.from_font(FONT, letter)
    if interpolated:
        return glyph.plot_interpolated(resolution)
    return glyph.plot()


def plot_font(interpolated: bool, resolution: int):
    font = Font(FONT)
    if interpolated:
        return font.plot_interpolated(resolution)
    return font.plot()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--letter", type=str, help="The single letter you want to plot")
    parser.add_argument(
        "--interpolated",
        action="store_true",
        help="Use this flag if you want to plot the interpolated points output by the GCode, not the Bezier curves.",
        default=False,
    )
    parser.add_argument(
        "--resolution",
        type=int,
        help="The number of points per Bezier curve to generate.",
        default=10,
    )
    args = parser.parse_args()

    if args.letter is None:
        plot_font(args.interpolated, args.resolution)
    else:
        plot_letter(args.letter, args.interpolated, args.resolution)
