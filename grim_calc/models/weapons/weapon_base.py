from bs4 import Tag
from grim_calc.models.base_modifier import DamageValueType, BaseValue, ValueSingle

from grim_calc.models.item_base import Item
from grim_calc.utils.globals import FLAT_DAMAGE_TYPES
from grim_calc.utils.html_utils import (
    remove_non_tags,
    get_child_tag_containing_class,
    get_child_tag_containing_string,
    strip_non_numeric,
)


class Weapon(Item):
    def __init__(
        self,
        div: Tag,
    ):
        super().__init__(div)
        self.item_base_stats = remove_non_tags(
            get_child_tag_containing_class(self.item_description, "item-base-stats")
        )
        attack_per_second_div = get_child_tag_containing_string(
            self.item_base_stats, "Attacks per Second"
        )
        self.base_damages = []
        self.attacks_per_second = strip_non_numeric(attack_per_second_div)
        for damage_name in FLAT_DAMAGE_TYPES:
            damage_div = get_child_tag_containing_string(
                self.item_base_stats, f"{damage_name} Damage"
            )
            if damage_div is not None:
                damage_range = str(damage_div).split("-")
                if len(damage_range) == 1:
                    damage_int = strip_non_numeric(damage_range)
                    damage_value = ValueSingle(damage_int)
                    self.base_damages.append(DamageValueType(damage_value, damage_name))
                else:
                    damage_min = strip_non_numeric(damage_range[0])
                    damage_max = strip_non_numeric(damage_range[1])
                    damage_value = BaseValue(
                        damage_min, damage_min, damage_max, damage_max
                    )
                    self.base_damages.append(DamageValueType(damage_value, damage_name))

        self.armor_piercing = 0
        armor_piercing_div = get_child_tag_containing_string(
            self.item_base_stats, "Armor Piercing"
        )
        if armor_piercing_div is not None:
            self.armor_piercing = strip_non_numeric(armor_piercing_div)
