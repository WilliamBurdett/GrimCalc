from typing import List, Type

from grim_calc.models.modifiers.base_damage_modifier import DamageModifier
from grim_calc.models.modifiers.base_modifier import FlatModifier, BaseModifier
from grim_calc.models.values import BaseValue, ValueSingle, ValueRange, ValueRanged


class InstantDamageModifier(DamageModifier, FlatModifier):
    name_to_replace = "InstantDamageModifier"
    value_sizes: List[Type[BaseValue]] = [ValueSingle, ValueRange, ValueRanged]


class PhysicalInstantDamageModifier(InstantDamageModifier):
    pass


class PierceInstantDamageModifier(InstantDamageModifier):
    pass


class FireInstantDamageModifier(InstantDamageModifier):
    pass


class ColdInstantDamageModifier(InstantDamageModifier):
    pass


class LightningInstantDamageModifier(InstantDamageModifier):
    pass


class AcidInstantDamageModifier(InstantDamageModifier):
    pass


class VitalityInstantDamageModifier(InstantDamageModifier):
    pass


class AetherInstantDamageModifier(InstantDamageModifier):
    pass


class ChaosInstantDamageModifier(InstantDamageModifier):
    pass


class ElementalInstantDamageModifier(InstantDamageModifier):
    pass


ORDER_OF_OPERATIONS = [
    PhysicalInstantDamageModifier,
    PierceInstantDamageModifier,
    FireInstantDamageModifier,
    ColdInstantDamageModifier,
    LightningInstantDamageModifier,
    AcidInstantDamageModifier,
    VitalityInstantDamageModifier,
    AetherInstantDamageModifier,
    ChaosInstantDamageModifier,
    ElementalInstantDamageModifier,
]
