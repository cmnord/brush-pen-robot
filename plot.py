from glyph import Glyph

if __name__ == "__main__":
    letter = "A"
    font = "fonts/cambam5.ttx"
    letter = Glyph.from_font(font, letter)
    letter.plot()
