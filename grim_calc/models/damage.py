from dataclasses import dataclass


@dataclass
class Attribute:
    minimum: int
    maximum: int


@dataclass
class Damage(Attribute):
    type_name: str


@dataclass
class FlatDamage(Damage):
    pass


@dataclass
class DotDamage(Damage):
    duration: int
