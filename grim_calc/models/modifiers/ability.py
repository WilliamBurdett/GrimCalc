from grim_calc.models.modifiers.base_modifier import (
    BaseModifier,
    FlatModifier,
    PercentModifier,
)
from grim_calc.models.values import BaseValue


class OffensiveModifier(BaseModifier):
    base_regex_parts = ["Offensive"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatOffensiveModifier(FlatModifier, OffensiveModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentOffensiveModifier(PercentModifier, OffensiveModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class DefensiveModifier(BaseModifier):
    base_regex_parts = ["Defensive"]

    def __init__(self, value: BaseValue):
        super().__init__(value)


class FlatDefensiveModifier(FlatModifier, DefensiveModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


class PercentDefensiveModifier(PercentModifier, DefensiveModifier):
    def __init__(self, value: BaseValue):
        super().__init__(value)


ORDER_OF_OPERATIONS = [
    FlatOffensiveModifier,
    PercentOffensiveModifier,
    FlatDefensiveModifier,
    PercentDefensiveModifier,
]
