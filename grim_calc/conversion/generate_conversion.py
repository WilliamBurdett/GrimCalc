"""
    https://www.youtube.com/watch?v=Nqf4PLpMNOU&list=PL-7HuL5PyGEKk8edrhehe9twkci1162Xp
    Order:
    1. Damage Skill Modifiers
    2. Local Skill Conversion (Items + Skill Modifier)
    3. Global Conversion (Auras + Items)
        A. Elemental to X comes before Fire/Cold/Lightning to X
        B. Damage to Elemental And Fire/Cold/Lightning Additive
    4. Armor Piercing (Only skills that have % weapon damage)
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List


@dataclass
class Damage:
    damage_type: str
    amount: float
    has_been_converted: bool = False


conversion_types = [
    "direct_skill_modifier",
    "global_elemental_to_x",
    "global",
    "armor_piercing",
]

@dataclass
class Conversion:
    conversion_type: str
    source_type: str
    target_type: str

    def perform_conversion(self, Damage) -> List[Damage]:
        pass


@dataclass
class Hit:
    damages: List[Damage]
    has_weapon_damage: bool


hit = Hit([Damage("physical", 100), Damage("acid", 100)], False)

import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)
qwe13