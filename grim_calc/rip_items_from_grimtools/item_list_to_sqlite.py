from bs4 import BeautifulSoup

from grim_calc.utils.html_utils import remove_non_tags


def main():
    with open(
        "/home/will/Code/GrimCalc/grim_calc/utils/rip_items_from_grimtools/raw_html/one_handed_swords.html",
        "r",
    ) as f:
        swords = f.read()
    soup = BeautifulSoup(swords.replace("\n", ""), "html.parser")
    children = remove_non_tags(soup.div.contents)
    for i in range(0, len(children), 2):
        header = children[i]
        items_div = children[i + 1]
        items = remove_non_tags(items_div.contents)
        rarity = header["class"][1]
        print(rarity)
        for item in items:

            print(item)


if __name__ == "__main__":
    main()
