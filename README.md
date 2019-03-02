# Brush pen lettering robot

## Development
1. create virtualenv
2. source virtualenv
3. `pip install -r requirements.txt`
4. use `ttx` command to convert any ttf font to ttx format
5. `python plot.py` to plot the letter A

## Helpful links
- [TrueType font encoding][ttf]
- [fonttools docs][fonttools] (converting to ttx)
- [Quadratic bezier][bez]
- [How OpenType works][otf]

[ttf]: https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=iws-chapter08
[fonttools]: https://pypi.org/project/fonttools/
[bez]: https://stackoverflow.com/questions/20733790/truetype-fonts-glyph-are-made-of-quadratic-bezier-why-do-more-than-one-consecu
[otf]: https://simoncozens.github.io/fonts-and-layout/opentype.html