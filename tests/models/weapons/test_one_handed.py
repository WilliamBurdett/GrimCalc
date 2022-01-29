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


class WeaponInitBaseStats(unittest.TestCase):
    @staticmethod
    def test_has_armor_piercing():
        example_tag = open_item_file("common_one_handed_sword")

        expected_armor_piercing = 10

        actual_sword = OneHandedSword(example_tag)
        assert expected_armor_piercing == actual_sword.armor_piercing

    @staticmethod
    def test_armor_piercing_defaults_to_0():
        example_tag = open_item_file("common_one_handed_axe")
        expected_armor_piercing = 0

        actual_axe = OneHandedAxe(example_tag)
        assert expected_armor_piercing == actual_axe.armor_piercing

    @staticmethod
    def test_gets_damage_range():
        example_tag = open_item_file("common_one_handed_axe")
        expected_damages = [
            Damage(9, 24, "Physical"),
        ]

        actual_axe = OneHandedMace(example_tag)
        assert expected_damages == actual_axe.base_damages

    @staticmethod
    def test_gets_damage_non_range():
        example_tag = open_item_file("common_one_handed_mace")
        expected_damages = [
            Damage(100, 100, "Physical"),
        ]

        actual_axe = OneHandedMace(example_tag)
        assert expected_damages == actual_axe.base_damages

    @staticmethod
    def test_gets_multiple_damages():
        example_tag = open_item_file("common_one_handed_sword")
        expected_damages = [
            Damage(12, 34, "Physical"),
            Damage(10, 10, "Fire"),
            Damage(5, 10, "Cold"),
        ]
        actual_sword = OneHandedSword(example_tag)
        assert expected_damages == actual_sword.base_damages


class WeaponInitAdditionalStats(unittest.TestCase):
    @staticmethod
    def test_gets_multiple_damages():
        example_tag = open_item_file("common_one_handed_scepter")
        expected_damages = [
            Damage(12, 34, "Physical"),
            Damage(10, 10, "Fire"),
            Damage(5, 10, "Cold"),
        ]
        actual_sword = OneHandedSword(example_tag)
        assert expected_damages == actual_sword.base_damages


if __name__ == "__main__":
    unittest.main()
