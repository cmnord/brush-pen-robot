from bs4 import BeautifulSoup

from glyph import Glyph


class Font:
    def __init__(self, filename: str):
        self.filename = filename
        with open(self.filename) as f:
            self.soup = BeautifulSoup(f, "xml")

        glyph_ids = self.soup.find("GlyphOrder").find_all("GlyphID")
        glyph_paths = self.soup.find("glyf")
        glyph_widths = self.soup.find("hmtx")
        height = int(self.soup.find("OS_2").find("sCapHeight")["value"])
        self.glyphs = {}
        for glyph_id in glyph_ids:
            name = glyph_id["name"]
            ttglyph = glyph_paths.find("TTGlyph", attrs={"name": name})
            width = int(glyph_widths.find("mtx", attrs={"name": name})["width"])
            self.glyphs[name] = Glyph(ttglyph, name, width, height)

    def get_glyph(self, name: str) -> Glyph:
        return self.glyphs.get(name)

    def plot(self):
        for glyph in self.glyphs:
            self.glyphs[glyph].plot()

