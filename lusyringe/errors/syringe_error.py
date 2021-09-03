from typing import Type


class LuSyringeError:
    def attribute_not_implemented(class_name: str, field: str, type_: Type):
        return NotImplementedError(
            f"Documentation for {field} with type {type_} was found,"
            f"but field was not implemented in {class_name}"
        )

    def illegal_type_attribution(field: str, applied_type: Type):
        return ValueError(
            f"Tried to apply type {applied_type} to already defined {field}"
            f"of another type"
        )
