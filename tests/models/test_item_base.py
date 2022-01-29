import unittest

import jsonpickle

from grim_calc.models.item_base import Item
from grim_calc.utils.serialization import encode
from tests.utils_for_tests import open_item_file


class BuildItemTests(unittest.TestCase):
    @staticmethod
    def test_item_init_happy_path():
        example_tag = open_item_file("basic_item")
        expected_rarity = "common"
        expected_name = "Scrapmetal Sawblade"
        expected_required_attributes = {"Physique": 26, "Item Level": 1}

        actual_item = Item(example_tag)
        assert actual_item.rarity == expected_rarity
        assert actual_item.name == expected_name
        assert actual_item.required_attributes == expected_required_attributes

    @staticmethod
    def test_picked_item_has_no_tags():
        example_tag = open_item_file("basic_item")
        actual_item = Item(example_tag)
        expected_pickle = {
            "py/object": "grim_calc.models.item_base.Item",
            "py/state": {
                "rarity": "common",
                "name": "Scrapmetal Sawblade",
                "required_attributes": {"Physique": 26, "Item Level": 1},
                "percent_damages": [],
                "conversions": [],
                "attribute_modifiers": [],
            },
        }
        actual_pickle = encode(actual_item)
        assert expected_pickle == actual_pickle


if __name__ == "__main__":
    unittest.main()
