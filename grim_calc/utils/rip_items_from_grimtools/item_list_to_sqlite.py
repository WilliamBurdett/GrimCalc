from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Iterable, Union, List, Tuple, Dict

from bs4 import BeautifulSoup, Tag, NavigableString


def remove_non_tags(all_children: List[Union[Tag, NavigableString]]) -> List[Tag]:
    children = []
    for child in all_children:
        if isinstance(child, Tag):
            children.append(child)
    return children


def get_child_tag_containing_class(contents: List[Tag], class_name: str) -> Tag:
    for tag in contents:
        if class_name in tag["class"]:
            return tag


@dataclass
class Item:
    rarity: str
    name: str
    minimum_level: int
    attribute_requirements: Dict[str, int]  # {"Cunning": 5}

    @staticmethod
    def get_class_params_from_tag(
        div: Tag,
    ) -> Tuple[str, str, int, Dict[str, int], List[Tag]]:
        inner_contents = remove_non_tags(div.div.contents)
        rarity = remove_non_tags(inner_contents[0].contents)[0]["class"][1].split("-")[
            1
        ]
        item_description = remove_non_tags(inner_contents[1].contents)
        name = item_description[0].contents[0].contents[0]
        return rarity, name, 0, {"": 1}, item_description


@dataclass
class Damage:
    minimum: int
    maximum: int
    type_name: str


@dataclass
class DotDamage(Damage):
    duration: int


@dataclass
class Weapon(Item):
    attack_speed: float
    damages: List[Damage]

    @staticmethod
    def get_class_params_from_tag(
        div: Tag,
    ) -> Tuple[str, str, float, List[Damage], Tag]:
        rarity, name, item_description = super().get_class_params_from_tag(div)
        attack_speed = float()
        damages = []

        attack_speed = item_description[2].contents[0].contents[0]
        return rarity, name, attack_speed, damages, item_description


@dataclass
class OneHandedSword(Weapon):
    pass


def build_item(item_description: Tag):
    pass


def parse_item(div: Tag) -> Item:
    inner_contents = remove_non_tags(div.div.contents)
    rarity = remove_non_tags(inner_contents[0].contents)[0]["class"][1].split("-")[1]
    item_description = remove_non_tags(inner_contents[1].contents)
    item_type = item_description[1].contents[0]
    type_map = {"One-Handed Sword": OneHandedSword}
    print(item_description)
    name = item_description[0].contents[0].contents[0]
    print(name)
    i = type_map[item_type](rarity, name)
    return i


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
