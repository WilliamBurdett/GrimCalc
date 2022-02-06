from dataclasses import dataclass

from grim_calc.models.base_modifier import ValueType


@dataclass
class Skill:
    name: str
    class_name: str


@dataclass
class SkillValueType(ValueType):
    skill: Skill
