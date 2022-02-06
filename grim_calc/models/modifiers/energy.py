from typing import Type

from grim_calc.models.modifiers.base_modifier import (
    BaseModifier,
    FlatModifier,
    PercentModifier,
)
from grim_calc.models.values import BaseValue, ValueOptions


class EnergyModifier(BaseModifier):
    base_regex_parts = ["Energy"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatEnergyModifier(FlatModifier, EnergyModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentEnergyModifier(PercentModifier, EnergyModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class EnergyRegeneratedModifier(BaseModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatEnergyRegeneratedModifier(FlatModifier, EnergyRegeneratedModifier):
    base_regex_parts = ["Energy Regenerated per Second"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentEnergyRegeneratedModifier(PercentModifier, EnergyRegeneratedModifier):
    base_regex_parts = ["Increases Energy Regeneration by "]

    def __init__(self, value: BaseValue):
        super().__init__(value)

    @classmethod
    def get_pattern(cls, value_size: Type[BaseValue], value_options: ValueOptions):
        return cls.get_pattern_value_last(value_size, value_options)
