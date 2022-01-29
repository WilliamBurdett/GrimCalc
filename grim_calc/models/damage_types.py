from dataclasses import dataclass


@dataclass
class DamageType:
    name: str
    needs_damage_for_flat: bool = True
    needs_damage_for_percent: bool = True

    def get_flat_str(self) -> str:
        suffix = ""
        if self.needs_damage_for_flat:
            suffix = " Damage"
        return f"{self.name}{suffix}"

    def get_percent_str(self) -> str:
        suffix = ""
        if self.needs_damage_for_percent:
            suffix = " Damage"
        return f"{self.name}{suffix}"


FLAT_DAMAGE_TYPES = (
    DamageType("Physical"),
    DamageType("Pierce"),
    DamageType("Fire"),
    DamageType("Cold"),
    DamageType("Lightning"),
    DamageType("Acid"),
    DamageType("Vitality"),
    DamageType("Aether"),
    DamageType("Chaos"),
    DamageType("Elemental"),
)


DOT_DAMAGE_TYPES = (
    DamageType("Internal Trauma", needs_damage_for_flat=False),
    DamageType("Bleeding"),
    DamageType("Burn"),
    DamageType("Frostburn"),
    DamageType("Electrocute"),
    DamageType("Poison"),
    DamageType("Vitality Decay", needs_damage_for_percent=False),
)
