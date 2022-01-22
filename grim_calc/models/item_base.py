from typing import Dict, Union

from bs4 import Tag

from grim_calc.utils.globals import ATTRIBUTES
from grim_calc.utils.html_utils import remove_non_tags, get_child_tag_containing_class, get_item_type


class Item:
    rarity: str
    name: str
    required_attributes: Dict[str, int]  # {"Cunning": 5, "Level": 5}

    def __init__(
        self,
        div: Tag,
    ):
        inner_contents = remove_non_tags(div.div.contents)
        rarity = remove_non_tags(inner_contents[0].contents)[0]["class"][1].split("-")[
            1
        ]
        item_description = remove_non_tags(inner_contents[1].contents)
        name = item_description[0].contents[0].contents[0]
        item_requirements = get_child_tag_containing_class(item_description, "item-req")
        required_attributes: Dict[str,int] = {}
        for requirement in remove_non_tags(item_requirements.contents):
            contents = requirement.contents[0]
            for attribute in ATTRIBUTES:
                if attribute in contents:
                    required_attributes[attribute] = int(contents.split(":")[1].strip())

        self.rarity = rarity
        self.name = name
        self.required_attributes: Dict[str,int] = required_attributes
        self.item_description = item_description
