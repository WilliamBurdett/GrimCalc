from grim_calc.utils.regex import camel_case_to_sentence


class DamageModifier:
    name_to_replace = "DamageModifier"
    needs_damage_for_flat = True
    needs_damage_for_percent = True

    @classmethod
    def get_name(cls) -> str:
        return camel_case_to_sentence(cls.__name__.replace(cls.name_to_replace, ""))

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

