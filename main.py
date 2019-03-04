from font import Font
from glyph import Glyph
import argparse

FONT = "fonts/cambam5.ttx"


def main(text: str, out_filename: str, resolution: int):
    font = Font(FONT)
    with open(out_filename, "w") as f:
        base_x = 0
        base_y = 0
        f.write("G1 Z{}".format(Glyph.Z_HIGH))
        # TODO: wrap text
        for char in text:
            f.write("G1 Z{}".format(Glyph.Z_LOW))
            glyph = font.get_glyph(char)
            gcode = glyph.get_gcode(base_x, base_y, resolution)
            f.write(gcode)
            f.write("G1 Z{}".format(Glyph.Z_HIGH))
            base_x += glyph.width * 0.8


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "text", type=str, help="The string you want to generate GCode for."
    )
    parser.add_argument(
        "--resolution",
        type=int,
        help="The number of points per Bezier curve to generate.",
        default=10,
    )
    parser.add_argument(
        "--out",
        type=str,
        help="The output file to write the GCode to.",
        default="examples/out.gcode",
    )
    args = parser.parse_args()
    main(args.text, args.out, args.resolution)
