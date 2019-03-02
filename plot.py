from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pdb

with open("a.xml") as f:
    soup = BeautifulSoup(f, "xml")

for contour in soup.find_all("contour"):
    pts = contour.find_all("pt")
    x = [int(pt["x"]) for pt in pts]
    x.append(x[0])
    y = [int(pt["y"]) for pt in pts]
    y.append(y[0])
    plt.plot(x, y)

plt.axis("equal")
plt.show()
