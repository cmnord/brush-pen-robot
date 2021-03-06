# Calligraphy Machine ✍️

![image 1](images/image1.jpg)

![image 2](images/image2.jpg)

![image 3](images/image3.jpg)

Made for [MakeMIT 2019][make].

## Development
1. create virtualenv
2. source virtualenv
3. `pip install -r requirements.txt`
4. use `ttx` command to convert any ttf font to ttx format
5. MacOS: fix matplotlib backend [bugfix][bug]

## Usage
- Generate GCode: see `python main.py -h` for options.
- Plot glyphs for testing: see `python plot.py -h` for options.

## Helpful links
- [TrueType font encoding][ttf]
- [fonttools docs][fonttools] (converting to ttx)
- [CamBam single-line fonts][cambam]
- [Quadratic bezier][bez]
- [How OpenType works][otf]

[make]: http://makemit.org/
[bug]: https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/
[ttf]: https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=iws-chapter08
[fonttools]: https://pypi.org/project/fonttools/
[cambam]: http://www.mrrace.com/CamBam_Fonts/
[bez]: https://stackoverflow.com/questions/20733790/truetype-fonts-glyph-are-made-of-quadratic-bezier-why-do-more-than-one-consecu
[otf]: https://simoncozens.github.io/fonts-and-layout/opentype.html
