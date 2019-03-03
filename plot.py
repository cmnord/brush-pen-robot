from font import Font


if __name__ == "__main__":
    font = Font("fonts/cambam5.ttx")
    letter = font.get_glyph("N")
    letter.plot()
