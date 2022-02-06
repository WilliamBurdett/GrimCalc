from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

from grim_calc.utils.regex import NUMBER_SINGLE


def get_number_single(include_plus: bool = False, include_ending_percent: bool = False):
    plus_prefix = ""
    if include_plus is True:
        plus_prefix = "\\+"
    ending_percent_suffix = ""
    if include_ending_percent is True:
        ending_percent_suffix = "%"
    return f"{plus_prefix}{NUMBER_SINGLE}{ending_percent_suffix}"


def get_number_range(include_plus: bool = False, include_ending_percent: bool = False):
    ending_percent_suffix = ""
    if include_ending_percent is True:
        ending_percent_suffix = "%"
    number = get_number_single(include_plus=include_plus, include_ending_percent=False)
    return f"{number}/{number}{ending_percent_suffix}"


def get_number_ranged(include_plus: bool = False):
    number = get_number_single(include_plus=include_plus, include_ending_percent=False)
    return f"({number})-({number})/({number})-({number})"


@dataclass
class ValueOptions:
    include_plus: bool
    include_ending_percent: bool


class BaseValue(ABC):
    constructor_count = 0

    @abstractmethod
    def __init__(self, *args: Union[str, float]):
        raise NotImplemented

    @abstractmethod
    def get_minimum(self) -> float:
        raise NotImplemented

    @abstractmethod
    def get_maximum(self) -> float:
        raise NotImplemented

    @abstractmethod
    def get_average(self) -> float:
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def get_regex(value_option: ValueOptions) -> str:
        return NotImplemented

    @abstractmethod
    def __str__(self) -> str:
        return NotImplemented


class ValueSingle(BaseValue):
    constructor_count = 1

    def __init__(self, value: Union[str, float]):
        self.value = value
        if isinstance(value, str):
            self.value = float(value)

    def get_minimum(self) -> float:
        return self.value

    def get_maximum(self) -> float:
        return self.value

    def get_average(self) -> float:
        return self.value

    @staticmethod
    def get_regex(value_option: ValueOptions) -> str:
        return get_number_single(
            value_option.include_plus, value_option.include_ending_percent
        )

    def __str__(self) -> str:
        return f"{self.value}"


class ValueRange(BaseValue):
    constructor_count = 2

    def __init__(self, min_value: Union[str, float], max_value: Union[str, float]):
        self.min_value = min_value
        if isinstance(min_value, str):
            self.min_value = float(min_value)
        self.max_value = max_value
        if isinstance(max_value, str):
            self.max_value = float(max_value)

    def get_minimum(self) -> float:
        return self.min_value

    def get_maximum(self) -> float:
        return self.max_value

    def get_average(self) -> float:
        return (self.min_value + self.max_value) / 2

    @staticmethod
    def get_regex(value_option: ValueOptions) -> str:
        return get_number_range(
            value_option.include_plus, value_option.include_ending_percent
        )

    def __str__(self) -> str:
        return f"{self.min_value}/{self.max_value}"


class ValueRanged(BaseValue):
    constructor_count = 4

    def __init__(
        self,
        l_min_value: Union[str, float],
        l_max_value: Union[str, float],
        u_min_value: Union[str, float],
        u_max_value: Union[str, float],
    ):
        self.l_min_value = l_min_value
        if isinstance(l_min_value, str):
            self.l_min_value = float(l_min_value)
        self.l_max_value = l_max_value
        if isinstance(l_max_value, str):
            self.l_max_value = float(l_max_value)
        self.u_min_value = u_min_value
        if isinstance(u_min_value, str):
            self.u_min_value = float(u_min_value)
        self.u_max_value = u_max_value
        if isinstance(u_max_value, str):
            self.u_max_value = float(u_max_value)

    def get_minimum(self) -> float:
        return self.l_min_value

    def get_maximum(self) -> float:
        return self.u_max_value

    def get_average(self) -> float:
        return (
            sum(
                [self.l_min_value, self.l_max_value, self.u_min_value, self.u_max_value]
            )
            / 4
        )

    @staticmethod
    def get_regex(value_option: ValueOptions) -> str:
        return get_number_ranged(value_option.include_plus)

    def __str__(self) -> str:
        return (
            f"{self.l_min_value}-{self.l_max_value}/"
            f"{self.u_min_value}-{self.u_max_value}"
        )
