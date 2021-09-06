from lusyringe.data.type_result import TypeResult
from typing import Type, Tuple


class __TypeChecker:
    def __get_annotations(self, attributes: dict) -> dict:
        return attributes['__annotations__']

    def exists_annotation(self, attributes: dict, field: str) -> bool:
        return field in self.__get_annotations(attributes)

    def attr_has_same_type(self, attributes: dict, field: str, type_: Type) -> TypeResult:
        if self.exists_annotation(attributes, field):
            existent_type = self.__get_annotations(attributes)[field]

            return TypeResult(
                has_same_type=existent_type == type_,
                existent_type=existent_type
            )

        return TypeResult(
            has_same_type=False,
            existent_type=None
        )

    def member_has_same_type(self, member: dict, field: str, type_: Type) -> TypeResult:
        return TypeResult(
            has_same_type=member[field] == type_,
            existent_type=member[field]
        )


TypeChecker = __TypeChecker()
