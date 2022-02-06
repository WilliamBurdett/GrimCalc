from typing import List, Type

from grim_calc.models.modifiers.base_damage_modifier import DamageModifier
from grim_calc.models.modifiers.base_modifier import FlatModifier, BaseModifier
from grim_calc.models.values import BaseValue, ValueSingle, ValueRange, ValueRanged


class InstantDamageModifier(DamageModifier, FlatModifier, BaseModifier):
    value_sizes: List[Type[BaseValue]] = [ValueSingle, ValueRange, ValueRanged]



class PhysicalDamageModifier(InstantDamageModifier):
    pass
class PierceDamageModifier(InstantDamageModifier):
    pass
class FireDamageModifier(InstantDamageModifier):
    pass
class ColdDamageModifier(InstantDamageModifier):
    pass
class LightningDamageModifier(InstantDamageModifier):
    pass
class AcidDamageModifier(InstantDamageModifier):
    pass
class VitalityDamageModifier(InstantDamageModifier):
    pass
class AetherDamageModifier(InstantDamageModifier):
    pass
class ChaosDamageModifier(InstantDamageModifier):
    pass
class ElementalDamageModifier(InstantDamageModifier):
    pass
