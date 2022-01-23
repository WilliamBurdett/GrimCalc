from dataclasses import dataclass


@dataclass
class Damage:
    minimum: int
    maximum: int
    type_name: str


@dataclass
class DotDamage(Damage):
    duration: int
