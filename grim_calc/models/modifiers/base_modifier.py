import re
from abc import ABC
from re import Pattern
from typing import List, Type, Any

from grim_calc.models.values import (
    BaseValue,
    ValueSingle,
    ValueRange,
    ValueOptions,
)


#
# class DamageValueType(ValueType):
#     damage_type: DamageType
#
#     def __post_init__(self):
#         if isinstance(self.damage_type, str):
#             self.damage_type = get_damage_type_from_name(self.damage_type)
#
# class PhysicalDamageModifier:
#     base_regex_parts: Tuple[str, ...] = ["Physical Damage"]
#
# class FlatPhysicalDamageModifier(PhysicalDamageModifier):
#     value_type = FlatValueType()
#
#
# class InstantDamageModifier:
#     base_regex_parts: Tuple[str, ...] = [get_regex_or_flat(INSTANT_DAMAGE_TYPES)]
#
# class DotDamageModifier:
#     base_regex_parts: Tuple[str, ...] = [get_regex_or_flat(DOT_DAMAGE_TYPES)]
#
#
#
# class InstantDamageValueType(FlatValueType, DamageValueType):
#     # 5 Physical Damage
#     # 1-2 Pierce Damage
#     # 1-2/3-4 Fire Damage
#     base_regex_parts: List[str] = [get_regex_or_flat(INSTANT_DAMAGE_TYPES)]
#     value_sizes: List[int]# = default_field([1,2,4])
#
#
#
# class DotDamageModifier(DamageValueType):
#     # 1 Bleeding Damage over 5 Seconds
#     # 1-2 Bleeding Damage over 5 Seconds
#     duration: int
#     regex_parts: List[str]# = default_field([get_regex_or_flat(DOT_DAMAGE_TYPES), "Over", NUMBER_SINGLE, "Seconds"])
#
#     def __post_init__(self):
#         if isinstance(self.duration, str):
#             self.duration = int(self.duration)
#
#
#
# class PercentDamageValueType(PercentValueType, DamageValueType):
#     # +10% Fire Damage # +10/+20% Fire Damage
#     regex_parts: List[str]# = default_field([get_regex_or_percent()])
#
#
#
# class ConversionValueType(PercentValueType):
#     source_damage_type: DamageType = None
#     target_damage_type: DamageType = None
#     regex_parts: List[str]# = default_field([
#             get_regex_or_percent(INSTANT_DAMAGE_TYPES),
#             "converted to",
#             get_regex_or_percent(INSTANT_DAMAGE_TYPES),
#         ])
#     value_sizes: List[int]# = default_field([2])
#
#     def __post_init__(self):
#         if isinstance(self.source_damage_type, str):
#             self.source_damage_type = get_damage_type_from_name(self.source_damage_type)
#         if isinstance(self.target_damage_type, str):
#             self.target_damage_type = get_damage_type_from_name(self.target_damage_type)
#
#
# def get_value_from_data_points(value_points: List[str]) -> BaseValue:
#     if len(value_points) == 1:
#         return ValueSingle(*value_points)
#     elif len(value_points) == 2:
#         return ValueRange(*value_points)
#     elif len(value_points) == 4:
#         return ValueRangedRange(*value_points)
#
#
# def get_global_modifier(
#     groups: Sequence[str], value_count: int, target_class: Type[ValueType]
# ) -> ValueType:
#     values = []
#     modifier_params = []
#     for index, value in enumerate(groups):
#         if index < value_count:
#             values.append(value)
#         else:
#             modifier_params.append(value)
#     return target_class(get_value_from_data_points(values), *modifier_params)
#
#
# VALUE_SIZE_MAP = {
#     1: get_number_single,
#     2: get_number_range,
#     4: get_number_ranged,
# }


# flat damage
# percent damage
# conversion
# health (flat or %?)
# energy (flat or %?)
# offensive
# defensive
# attack, cast, total, movement speed
# health regen (flat before %)
# energy regen (flat before %)
# resistances
#


class BaseModifier(ABC):
    base_regex_parts: List[str] = []
    value_sizes: List[Type[BaseValue]] = [ValueSingle, ValueRange]
    value_options: ValueOptions = None

    def __init__(self, value: BaseValue, *args: Any):
        self.value = value

    @classmethod
    def get_pattern(
        cls, value_size: Type[BaseValue], value_options: ValueOptions
    ) -> Pattern:
        return cls.get_pattern_value_first(value_size, value_options)

    @classmethod
    def get_pattern_value_first(
        cls, value_size: Type[BaseValue], value_options: ValueOptions
    ) -> Pattern:
        return re.compile(
            " ".join(
                [
                    value_size.get_regex(value_options),
                    *cls.base_regex_parts,
                ]
            )
        )

    @classmethod
    def get_pattern_value_last(
        cls, value_size: Type[BaseValue], value_options: ValueOptions
    ) -> Pattern:
        return re.compile(
            " ".join(
                [
                    *cls.base_regex_parts,
                    value_size.get_regex(value_options),
                ]
            )
        )


class FlatModifier:
    value_options = ValueOptions(True, False)


class PercentModifier:
    value_options = ValueOptions(True, True)
