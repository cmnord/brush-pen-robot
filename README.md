# Calligraphy Machine ✍️

![image 1](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/773/630/datas/gallery.jpg)

![image 2](https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/773/608/datas/gallery.jpg)

## Development
1. create virtualenv
2. source virtualenv
3. `pip install -r requirements.txt`
4. use `ttx` command to convert any ttf font to ttx format
5. MacOS: fix matplotlib backend [bugfix][bug]
6. `python plot.py` to plot the letter A

## Helpful links
- [TrueType font encoding][ttf]
- [fonttools docs][fonttools] (converting to ttx)
- [CamBam single-line fonts][cambam]
- [Quadratic bezier][bez]
- [How OpenType works][otf]

[bug]: https://markhneedham.com/blog/2018/05/04/python-runtime-error-osx-matplotlib-not-installed-as-framework-mac/
[ttf]: https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=iws-chapter08
[fonttools]: https://pypi.org/project/fonttools/
[cambam]: http://www.mrrace.com/CamBam_Fonts/
[bez]: https://stackoverflow.com/questions/20733790/truetype-fonts-glyph-are-made-of-quadratic-bezier-why-do-more-than-one-consecu
[otf]: https://simoncozens.github.io/fonts-and-layout/opentype.html
