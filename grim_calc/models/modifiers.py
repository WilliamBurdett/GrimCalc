from abc import ABC
from dataclasses import dataclass
from typing import List, Callable

from bs4 import Tag

from grim_calc.models.damage_types import (
    FLAT_DAMAGE_TYPES,
    DOT_DAMAGE_TYPES,
    DamageType,
)
from grim_calc.utils.html_utils import strip_non_numeric


@dataclass
class BaseValue(ABC):
    pass


@dataclass
class ValueSingle(BaseValue):
    value: int


@dataclass
class ValueWithRange(BaseValue):
    min_value: int
    max_value: int


@dataclass
class ValueWithRangedValues(BaseValue):
    l_min_value: int
    l_max_value: int
    u_min_value: int
    u_max_value: int


@dataclass
class Modifier:
    value: BaseValue


@dataclass
class DamageModifier(Modifier):
    damage_type: DamageType


@dataclass
class FlatDamageModifier(DamageModifier):
    pass


@dataclass
class DotDamageModifier(DamageModifier):
    duration: int


@dataclass
class PercentDamageModifier(DamageModifier):
    pass


def get_direct_damage_modifiers(
    modifier_divs: List[Tag],
    div_index: int,
    flat_damage_types: List[DamageType] = FLAT_DAMAGE_TYPES,
    dot_damage_types: List[DamageType] = DOT_DAMAGE_TYPES,
):
    direct_damage_modifiers = []
    for damage_type in [*flat_damage_types, *dot_damage_types]:
        modifier_str = str(modifier_divs[div_index]).strip()
        if modifier_str.endswith(damage_type.get_flat_str()) or (
            damage_type.get_flat_str in modifier_str
            and modifier_str.endswith("Seconds")
        ):
            direct_damage_modifiers.append(
                get_direct_damage_modifier(modifier_str, damage_type)
            )
            div_index += 1
    return direct_damage_modifiers, div_index


def get_percent_damage_modifiers(
    modifier_divs: List[Tag],
    div_index: int,
    flat_damage_types: List[DamageType] = FLAT_DAMAGE_TYPES,
    dot_damage_types: List[DamageType] = DOT_DAMAGE_TYPES,
):
    percent_damage_modifiers = []
    for damage_type in [*flat_damage_types, *dot_damage_types]:
        modifier_str = str(modifier_divs[div_index]).strip()
        if modifier_str.endswith(damage_type.get_percent_str()):
            percent_damage_modifiers.append(
                get_percent_damage_modifier(modifier_str, damage_type)
            )
            div_index += 1
    return percent_damage_modifiers, div_index


def get_value_with_ranged_values(damage_str: str) -> ValueWithRangedValues:
    min_range, max_range = damage_str.split("/")
    l_min_str, l_max_str = min_range.split("-")
    u_min_str, u_max_str = max_range.split("-")
    return ValueWithRangedValues(
        strip_non_numeric(l_min_str),
        strip_non_numeric(l_max_str),
        strip_non_numeric(u_min_str),
        strip_non_numeric(u_max_str),
    )


def get_value_with_range(damage_str: str) -> ValueWithRange:
    split_char = "-"
    if "/" in damage_str:
        split_char = "/"
    min_str, max_str = damage_str.split(split_char)
    return ValueWithRange(
        strip_non_numeric(min_str),
        strip_non_numeric(max_str),
    )


def get_value_single(damage_str: str) -> ValueSingle:
    return ValueSingle(strip_non_numeric(damage_str))


def get_base_value(inner_html: str) -> BaseValue:
    damage_str = inner_html.split(" ")[0].strip()
    if "/" in damage_str and "-" in damage_str:
        "<div>1-2/3-4 Vitality Damage</div>"
        return get_value_with_ranged_values(damage_str)
    elif "-" in damage_str or "/" in damage_str:
        "<div>1-2 Pierce Damage</div>"
        return get_value_with_range(damage_str)
    return ValueSingle(strip_non_numeric(damage_str))


def get_direct_damage_modifier(
    inner_html: str, damage_type: DamageType
) -> DamageModifier:
    value = get_base_value(inner_html)
    if "over" in inner_html:
        DotDamageModifier(
            value, damage_type, strip_non_numeric(inner_html.split("over")[1])
        )
    return FlatDamageModifier(value, damage_type)


def get_percent_damage_modifier(
    inner_html: str, damage_type: DamageType
) -> PercentDamageModifier:
    value = get_base_value(inner_html)
    return PercentDamageModifier(value, damage_type)


ORDER_OF_OPERATIONS = (get_direct_damage_modifiers, get_percent_damage_modifiers)


def get_modifiers(
    modifier_divs: List[Tag], order_of_operations: List[Callable] = ORDER_OF_OPERATIONS
) -> List[Modifier]:
    div_index = 0
    modifiers: List[Modifier] = []
    for operation in order_of_operations:
        modifiers_for_operation, div_index = operation(modifier_divs, div_index)
        modifiers.extend(modifiers_for_operation)
    return modifiers
