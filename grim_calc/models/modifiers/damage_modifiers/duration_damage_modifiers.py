import re
from re import Pattern
from typing import Type

from grim_calc.models.modifiers.base_damage_modifier import DamageModifier
from grim_calc.models.modifiers.base_modifier import FlatModifier, BaseModifier
from grim_calc.models.values import BaseValue, ValueSingle, ValueOptions
from grim_calc.utils.regex import NUMBER_SINGLE


class DurationDamageModifier(
    FlatModifier,
    DamageModifier,
):
    name_to_replace = "DurationDamageModifier"

    def __init__(self, value: BaseValue, duration: ValueSingle):
        super().__init__(value)
        self.duration = duration

    @classmethod
    def get_pattern(
        cls, value_size: Type[BaseValue], value_options: ValueOptions
    ) -> Pattern:
        return re.compile(
            " ".join(
                [
                    cls.get_flat_str().replace(cls.name_to_replace, ""),
                    "Over",
                    NUMBER_SINGLE,
                    "Seconds",
                ]
            )
        )


class InternalTraumaDurationDamageModifier(DurationDamageModifier):
    needs_damage_for_flat = False


class BleedingDurationDamageModifier(DurationDamageModifier):
    pass


class BurnDurationDamageModifier(DurationDamageModifier):
    pass


class FrostburnDurationDamageModifier(DurationDamageModifier):
    pass


class ElectrocuteDurationDamageModifier(DurationDamageModifier):
    pass


class PoisonDurationDamageModifier(DurationDamageModifier):
    pass


class VitalityDecayDurationDamageModifier(DurationDamageModifier):
    needs_damage_for_flat = False


ORDER_OF_OPERATIONS = [
    InternalTraumaDurationDamageModifier,
    BleedingDurationDamageModifier,
    BurnDurationDamageModifier,
    FrostburnDurationDamageModifier,
    ElectrocuteDurationDamageModifier,
    PoisonDurationDamageModifier,
    VitalityDecayDurationDamageModifier,
]
