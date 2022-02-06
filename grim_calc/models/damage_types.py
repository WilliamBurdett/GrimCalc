class DamageType:
    needs_damage_for_flat = True
    needs_damage_for_percent = True

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__

    @classmethod
    def get_flat_str(cls) -> str:
        suffix = ""
        if cls.needs_damage_for_flat:
            suffix = " Damage"
        return f"{cls.get_name()}{suffix}"

    @classmethod
    def get_percent_str(cls) -> str:
        suffix = ""
        if cls.needs_damage_for_percent:
            suffix = " Damage"
        return f"{cls.get_name()}{suffix}"


#
# INSTANT_DAMAGE_TYPES = (
#     DamageType("Physical"),
#     DamageType("Pierce"),
#     DamageType("Fire"),
#     DamageType("Cold"),
#     DamageType("Lightning"),
#     DamageType("Acid"),
#     DamageType("Vitality"),
#     DamageType("Aether"),
#     DamageType("Chaos"),
#     DamageType("Elemental"),
# )
#
#
# DOT_DAMAGE_TYPES = (
#     DamageType("Internal Trauma", needs_damage_for_flat=False),
#     DamageType("Bleeding"),
#     DamageType("Burn"),
#     DamageType("Frostburn"),
#     DamageType("Electrocute"),
#     DamageType("Poison"),
#     DamageType("Vitality Decay", needs_damage_for_percent=False),
# )

#
# def get_damage_type_from_name(
#     damage_type_name: str,
#     instant_damage_types: Iterable[DamageType] = INSTANT_DAMAGE_TYPES,
#     dot_damage_types: Iterable[DamageType] = DOT_DAMAGE_TYPES,
# ) -> DamageType:
#     for damage_type in [*instant_damage_types, *dot_damage_types]:
#         if damage_type_name in [
#             damage_type.name,
#             damage_type.get_flat_str(),
#             damage_type.get_percent_str(),
#         ]:
#             return damage_type
#
#
# def get_regex_or_percent(
#     damage_types: Iterable[DamageType] = (*INSTANT_DAMAGE_TYPES, *DOT_DAMAGE_TYPES)
# ) -> str:
#     regex_or = "|".join([damage_type.get_percent_str() for damage_type in damage_types])
#     return f"({regex_or})"
#
#
# def get_regex_or_flat(
#     damage_types: Iterable[DamageType] = (*INSTANT_DAMAGE_TYPES, *DOT_DAMAGE_TYPES)
# ) -> str:
#     regex_or = "|".join([damage_type.get_flat_str() for damage_type in damage_types])
#     return f"({regex_or})"
