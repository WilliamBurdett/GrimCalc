import re
from re import Pattern
from typing import Type

from grim_calc.models.modifiers.base_damage_modifier import DamageModifier
from grim_calc.models.modifiers.base_modifier import FlatModifier, BaseModifier
from grim_calc.models.values import BaseValue, ValueSingle, ValueOptions
from grim_calc.utils.regex import NUMBER_SINGLE


class DurationDamageModifier(
    DamageModifier,
    FlatModifier,
    BaseModifier,
):
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

class InternalTraumaDamageModifier(DurationDamageModifier):
    needs_damage_for_flat = False
class BleedingDamageModifier(DurationDamageModifier):
    pass
class BurnDamageModifier(DurationDamageModifier):
    pass
class FrostburnDamageModifier(DurationDamageModifier):
    pass
class ElectrocuteDamageModifier(DurationDamageModifier):
    pass
class PoisonDamageModifier(DurationDamageModifier):
    pass
class VitalityDecayDamageModifier(DurationDamageModifier):
    needs_damage_for_flat = False

