from dataclasses import dataclass


class Attribute:
    def __init__(self, attribute_type: str):
        self.attribute_type = attribute_type

class ConversionAttribute(Attribute):
    def __init__(self, attribute_type: str):
        super().__init__(attribute_type)
