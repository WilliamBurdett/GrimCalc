import unittest
from typing import Dict

from grim_calc.models.item_base import Item
from tests.utils_for_tests import open_item_file


def assert_item(
    actual_item: Item,
    expected_rarity: str,
    expected_name: str,
    expected_required_attributes: Dict[str, int],
):
    assert actual_item.rarity == expected_rarity
    assert actual_item.name == expected_name
    assert actual_item.required_attributes == expected_required_attributes


class BuildItemTests(unittest.TestCase):
    @staticmethod
    def test_item_init_happy_path():
        example_tag = open_item_file("basic_item")
        expected_rarity = "common"
        expected_name = "Scrapmetal Sawblade"
        expected_required_attributes = {"Physique": 26, "Item Level": 1}

        actual_sword = Item(example_tag)
        assert_item(
            actual_sword, expected_rarity, expected_name, expected_required_attributes
        )

if __name__ == "__main__":
    unittest.main()
