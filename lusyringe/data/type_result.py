from typing import Optional, Type


class TypeResult:
    has_same_type: bool
    existent_type: Optional[bool]

    def __init__(self, has_same_type: bool = False, existent_type: Type = None):
        self.has_same_type = has_same_type
        self.existent_type = existent_type
