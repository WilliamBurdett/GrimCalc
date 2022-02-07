from typing import List, Type

from grim_calc.models.modifiers.ability import (
    ORDER_OF_OPERATIONS as ABILITY_ORDER_OF_OPERATIONS,
)
from grim_calc.models.modifiers.base_modifier import BaseModifier
from grim_calc.models.modifiers.energy import (
    ORDER_OF_OPERATIONS as ENERGY_ORDER_OF_OPERATIONS,
)
from grim_calc.models.modifiers.health import (
    ORDER_OF_OPERATIONS as HEALTH_ORDER_OF_OPERATIONS,
)
from grim_calc.models.modifiers.damage_modifiers.instant_damge_modifiers import (
    ORDER_OF_OPERATIONS as INSTANT_DAMAGE_ORDER_OF_OPERATIONS,
)
from grim_calc.models.modifiers.damage_modifiers.duration_damage_modifiers import (
    ORDER_OF_OPERATIONS as DURATION_DAMAGE_ORDER_OF_OPERATIONS,
)
from grim_calc.models.modifiers.damage_modifiers.percent_damage_modifiers import (
    ORDER_OF_OPERATIONS as PERCENT_DAMAGE_ORDER_OF_OPERATIONS,
)

ORDER_OF_OPERATIONS = (
    *INSTANT_DAMAGE_ORDER_OF_OPERATIONS,
    *DURATION_DAMAGE_ORDER_OF_OPERATIONS,
    *PERCENT_DAMAGE_ORDER_OF_OPERATIONS,
    # conversion
    *HEALTH_ORDER_OF_OPERATIONS,
    *ENERGY_ORDER_OF_OPERATIONS,
    *ABILITY_ORDER_OF_OPERATIONS,
)


def get_modifiers_from_str(
    raw_modifiers: List[str],
    order_of_modifiers: List[Type[BaseModifier]] = ORDER_OF_OPERATIONS,
) -> List[BaseModifier]:
    modifier_index = 0
    modifiers: List[BaseModifier] = []
    for modifier in order_of_modifiers:
        for value_size_class in modifier.value_sizes:
            pattern = modifier.get_pattern(value_size_class, modifier.value_options)
            while True:
                modifier_str = raw_modifiers[modifier_index].strip()
                match = pattern.match(modifier_str)
                if match is not None:
                    value_size_params = []
                    modifier_params = []
                    for index, item in enumerate(match.groups()):
                        if index < value_size_class.constructor_count:
                            value_size_params.append(item)
                        else:
                            modifier_params.append(item)
                    modifiers.append(
                        modifier(value_size_class(*value_size_params), *modifier_params)
                    )
                    modifier_index += 1
                    if modifier_index > len(raw_modifiers) - 1:
                        return modifiers
                else:
                    break
    return modifiers
