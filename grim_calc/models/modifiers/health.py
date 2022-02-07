from typing import Type

from grim_calc.models.modifiers.base_modifier import (
    BaseModifier,
    FlatModifier,
    PercentModifier,
)
from grim_calc.models.values import BaseValue, ValueOptions


class HealthModifier(BaseModifier):
    base_regex_parts = ["Health"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatHealthModifier(FlatModifier, HealthModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentHealthModifier(PercentModifier, HealthModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class HealthRegeneratedModifier(BaseModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatHealthRegeneratedModifier(FlatModifier, HealthRegeneratedModifier):
    base_regex_parts = ["Health Regenerated per Second"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentHealthRegeneratedModifier(PercentModifier, HealthRegeneratedModifier):
    base_regex_parts = ["Increases Health Regeneration by "]

    def __init__(self, value: BaseValue):
        super().__init__(value)

    @classmethod
    def get_pattern(cls, value_size: Type[BaseValue], value_options: ValueOptions):
        return cls.get_pattern_value_last(value_size, value_options)


ORDER_OF_OPERATIONS = [
    FlatHealthModifier,
    PercentHealthModifier,
    FlatHealthRegeneratedModifier,
    PercentHealthRegeneratedModifier,
]
