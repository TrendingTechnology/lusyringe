
from typing import Any, Type


class Prescription:
    field: str
    type: Type
    doc: Any

    def __init__(self, field: str, type: Type, doc: Any):
        self.field = field
        self.type = type
        self.doc = doc
