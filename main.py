from font import Font

FONT = "fonts/cambam5.ttx"


def main(text: str, out_filename: str, resolution: int):
    font = Font(FONT)
    with open(out_filename, "w") as f:
        base_x = 0
        base_y = 0
        # TODO: wrap text
        for char in text:
            if char not in font.glyphs:
                print("skipping unsupported char '{}'".format(char))
                continue
            glyph = font.get_glyph(char)
            gcode = glyph.get_gcode(base_x, base_y, resolution)
            f.write(gcode)
            base_x += glyph.width
            # base_y += glyph.height


if __name__ == "__main__":
    text = "MakeMIT"
    resolution = 10
    main(text, "examples/makemit.gcode", resolution)
