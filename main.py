from font import Font


def main(text: str, font_filename: str, out_filename: str):
    font = Font(font_filename)
    with open(out_filename, "w") as f:
        base_x = 0
        base_y = 0
        # TODO: wrap text
        for char in text:
            glyph = font.get_glyph(char)
            gcode = glyph.get_gcode(base_x, base_y)
            f.write(gcode)
            base_x += glyph.width
            # base_y += glyph.height


if __name__ == "__main__":
    main("Hello MakeMIT!", "fonts/cambam5.ttx", "a.out")
