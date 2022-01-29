from dataclasses import dataclass

from grim_calc.models.modifiers import Modifier


@dataclass
class Skill:
    name: str
    class_name: str


@dataclass
class SkillModifier(Modifier):
    skill: Skill
