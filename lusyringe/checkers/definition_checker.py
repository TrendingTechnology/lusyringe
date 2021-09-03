import inspect

from typing import Tuple, Type

from .type_checker import TypeChecker


class __DefinitionChecker:
    def __init__(self, type_checker: TypeChecker):
        self.type_checker = type_checker

    def defined_in_attributes(self, attributes: dict, field: str, type_: Type) -> bool:
        has_same_type = self.type_checker.attr_has_same_type(
            attributes,
            field,
            type_
        )

        return has_same_type

    def defined_in_class(self, class_: Type, field: str, type_: Type) -> bool:
        members = inspect.getmembers(
            class_,
            lambda member: type(member) is dict and field in member
        )

        if len(members) > 0:
            member_attributes = members[0][1]

            return self.type_checker.member_has_same_type(
                member_attributes,
                field,
                type_
            )

        return False

    def defined_in_bases(self, field: str, type_: Type, bases: Tuple[Type]) -> bool:
        if not bases:
            return False

        found = False

        for base in bases:
            if self.defined_in_class(base, field, type_):
                return True

            found = self.defined_in_bases(
                field,
                type_,
                base.__bases__
            )

            if found:
                return True

        return False


DefinitionChecker = __DefinitionChecker(TypeChecker)
