import os
import unittest
from typing import Dict, List, Union

from bs4 import BeautifulSoup, Tag

from grim_calc.models.damage import Damage
from grim_calc.models.item_base import Item
from grim_calc.models.weapons.one_handed import (
    OneHandedMace,
    OneHandedAxe,
    OneHandedSword,
)
from grim_calc.models.weapons.weapon_base import Weapon
from tests.utils_for_tests import open_item_file


def assert_weapon(
    actual_weapon: Weapon,
    expected_damages: List[Damage],
    expected_attacks_per_second: Union[float, int],
    expected_armor_piercing: int,
):
    assert actual_weapon.damages == expected_damages
    assert actual_weapon.attacks_per_second == expected_attacks_per_second
    assert actual_weapon.armor_piercing == expected_armor_piercing


class BuildItemTests(unittest.TestCase):
    @staticmethod
    def test_build_item_one_handed_sword_happy_path():
        example_tag = open_item_file("one_handed_sword")
        expected_damages = [
            Damage(12, 34, "Physical"),
            Damage(10, 10, "Fire"),
            Damage(5, 10, "Cold"),
        ]
        expected_attacks_per_second = 1.88
        expected_armor_piercing = 10

        actual_sword = OneHandedSword(example_tag)
        assert_weapon(
            actual_sword,
            expected_damages,
            expected_attacks_per_second,
            expected_armor_piercing,
        )

    @staticmethod
    def test_build_item_one_handed_axe_happy_path():
        example_tag = open_item_file("one_handed_axe")
        expected_damages = [
            Damage(9, 24, "Physical"),
        ]
        expected_attacks_per_second = 1.86
        expected_armor_piercing = 0

        actual_axe = OneHandedAxe(example_tag)
        assert_weapon(
            actual_axe,
            expected_damages,
            expected_attacks_per_second,
            expected_armor_piercing,
        )

    @staticmethod
    def test_build_item_one_handed_mace_happy_path():
        example_tag = open_item_file("one_handed_mace")
        expected_damages = [
            Damage(13, 251, "Physical"),
        ]
        expected_attacks_per_second = 1.64
        expected_armor_piercing = 0

        actual_axe = OneHandedMace(example_tag)
        assert_weapon(
            actual_axe,
            expected_damages,
            expected_attacks_per_second,
            expected_armor_piercing,
        )


if __name__ == "__main__":
    unittest.main()
