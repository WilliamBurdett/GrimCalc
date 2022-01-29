from typing import Dict, List

from bs4 import Tag

from grim_calc.utils.globals import ATTRIBUTES
from grim_calc.utils.html_utils import (
    get_child_tag_containing_class,
    get_child_tag_containing_string,
    remove_all_tags_of_type,
    get_contents,
)


class Item:
    def __init__(self, div: Tag):
        remove_all_tags_of_type(div, "span")
        item_card = get_contents(div.div)
        item_description = get_contents(
            get_child_tag_containing_class(item_card, "item-description")
        )

        self.rarity = Item.parse_rarity_from_item_card(item_card)
        self.name = Item.parse_name_from_item_description(item_description)
        self.required_attributes = Item.parse_required_attributes_from_item_description(
            item_description
        )
        self.item_description = item_description
        self.attribute_modifiers = []

    @staticmethod
    def parse_rarity_from_item_card(item_card: List[Tag]) -> str:
        item_bitmap_div = get_child_tag_containing_class(
            item_card, "item-bitmap-container"
        )
        item_bitmap_contents = get_contents(item_bitmap_div)
        item_bitmap_background_div = get_child_tag_containing_class(
            item_bitmap_contents, "item-bitmap-background"
        )
        for class_name in item_bitmap_background_div["class"]:
            if "bg-" in class_name:
                return class_name.split("-")[1]

    @staticmethod
    def parse_name_from_item_description(item_description: List[Tag]) -> str:
        name_div = get_child_tag_containing_string(item_description, "item-name")
        remove_all_tags_of_type(name_div, "a")
        return str(name_div.contents[0])

    @staticmethod
    def parse_required_attributes_from_item_description(
        item_description: List[Tag],
    ) -> Dict[str, int]:
        item_requirements = get_child_tag_containing_class(item_description, "item-req")
        required_attributes: Dict[str, int] = {}
        for requirement in get_contents(item_requirements):
            contents = requirement.contents[0]
            for attribute in ATTRIBUTES:
                if attribute in contents:
                    required_attributes[attribute] = int(contents.split(":")[1].strip())
        return required_attributes

    def __getstate__(self):
        """Return state values to be pickled."""
        state = self.__dict__.copy()
        for key in list(state.keys()):
            if isinstance(state[key], Tag):
                del state[key]
            if isinstance(state[key], list):
                if len(state[key]) > 0:
                    if isinstance(state[key][0], Tag):
                        del state[key]
        return state
