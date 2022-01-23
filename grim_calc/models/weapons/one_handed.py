from bs4 import Tag

from grim_calc.models.weapons.weapon_base import Weapon


class OneHandedSword(Weapon):
    def __init__(
        self,
        div: Tag,
    ):
        super().__init__(div)


class OneHandedAxe(Weapon):
    def __init__(
        self,
        div: Tag,
    ):
        super().__init__(div)


class OneHandedMace(Weapon):
    def __init__(
        self,
        div: Tag,
    ):
        super().__init__(div)
