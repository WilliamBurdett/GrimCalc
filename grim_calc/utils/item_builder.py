from typing import Dict, Union

from bs4 import Tag

from grim_calc.models.weapons.one_handed import OneHandedSword, OneHandedAxe, OneHandedMace
from grim_calc.utils.globals import ATTRIBUTES
from grim_calc.utils.html_utils import remove_non_tags, get_child_tag_containing_class, get_item_type



def build_item_from_tag(div: Tag) -> Union[OneHandedSword, OneHandedAxe, OneHandedMace]:
    for match in div.findAll("span"):
        match.unwrap()
    item_type = get_item_type(div)
    type_map = {"One-Handed Sword": OneHandedSword,
                "One-Handed Axe": OneHandedAxe,
                "One-Handed Mace": OneHandedMace,
                }
    item = type_map[item_type](div)
    return item