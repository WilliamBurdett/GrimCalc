from grim_calc.models.modifiers.base_damage_modifier import DamageModifier
from grim_calc.models.modifiers.base_modifier import PercentModifier, BaseModifier
from grim_calc.models.values import ValueSingle


class PercentDamageModifier(
    PercentModifier,
    DamageModifier,
):
    name_to_replace = "PercentDamageModifier"


class PhysicalPercentDamageModifier(PercentDamageModifier):
    pass


class PiercePercentDamageModifier(PercentDamageModifier):
    pass


class FirePercentDamageModifier(PercentDamageModifier):
    pass


class ColdPercentDamageModifier(PercentDamageModifier):
    pass


class LightningPercentDamageModifier(PercentDamageModifier):
    pass


class AcidPercentDamageModifier(PercentDamageModifier):
    pass


class VitalityPercentDamageModifier(PercentDamageModifier):
    pass


class AetherPercentDamageModifier(PercentDamageModifier):
    pass


class ChaosPercentDamageModifier(PercentDamageModifier):
    pass


class ElementalPercentDamageModifier(PercentDamageModifier):
    pass


class InternalTraumaPercentDamageModifier(PercentDamageModifier):
    needs_damage_for_flat = False


class BleedingPercentDamageModifier(PercentDamageModifier):
    pass


class BurnPercentDamageModifier(PercentDamageModifier):
    pass


class FrostburnPercentDamageModifier(PercentDamageModifier):
    pass


class ElectrocutePercentDamageModifier(PercentDamageModifier):
    pass


class PoisonPercentDamageModifier(PercentDamageModifier):
    pass


class VitalityDecayPercentDamageModifier(PercentDamageModifier):
    needs_damage_for_percent = False


ORDER_OF_OPERATIONS = [
    PhysicalPercentDamageModifier,
    PiercePercentDamageModifier,
    FirePercentDamageModifier,
    ColdPercentDamageModifier,
    LightningPercentDamageModifier,
    AcidPercentDamageModifier,
    VitalityPercentDamageModifier,
    AetherPercentDamageModifier,
    ChaosPercentDamageModifier,
    ElementalPercentDamageModifier,
    InternalTraumaPercentDamageModifier,
    BleedingPercentDamageModifier,
    BurnPercentDamageModifier,
    FrostburnPercentDamageModifier,
    ElectrocutePercentDamageModifier,
    PoisonPercentDamageModifier,
    VitalityDecayPercentDamageModifier,
]
