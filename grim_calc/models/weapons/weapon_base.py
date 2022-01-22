from bs4 import Tag

from grim_calc.models.damage import Damage
from grim_calc.models.item_base import Item
from grim_calc.utils.globals import DIRECT_DAMAGE_TYPES
from grim_calc.utils.html_utils import remove_non_tags, get_child_tag_containing_class, get_child_tag_containing_string, \
    strip_non_numeric


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
        self.damages = []
        self.attacks_per_second = strip_non_numeric(attack_per_second_div)
        for damage_name in DIRECT_DAMAGE_TYPES:
            damage_div = get_child_tag_containing_string(
                self.item_base_stats, f"{damage_name} Damage"
            )
            if damage_div is not None:
                damage_range = str(damage_div).split("-")
                if len(damage_range) == 1:
                    damage_value = strip_non_numeric(damage_range)
                    self.damages.append(Damage(damage_value, damage_value, damage_name))
                else:
                    damage_min = strip_non_numeric(damage_range[0])
                    damage_max = strip_non_numeric(damage_range[1])
                    self.damages.append(Damage(damage_min, damage_max, damage_name))

        self.armor_piercing = 0
        armor_piercing_div = get_child_tag_containing_string(
            self.item_base_stats, "Armor Piercing"
        )
        if armor_piercing_div is not None:
            self.armor_piercing = strip_non_numeric(armor_piercing_div)