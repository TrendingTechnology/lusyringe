from typing import Optional, Type


class CheckerResult:
    is_defined: bool
    has_same_type: bool
    existent_type: Optional[Type]

    def __init__(self, is_defined: bool = False, has_same_type: bool = False, existent_type: Optional[Type] = False):
        self.is_defined = is_defined
        self.has_same_type = has_same_type
        self.existent_type = existent_type
