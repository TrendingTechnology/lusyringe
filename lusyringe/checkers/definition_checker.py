import inspect

from typing import Tuple, Type

from .type_checker import TypeChecker

from ..data import CheckerResult


class __DefinitionChecker:
    def __init__(self, type_checker: TypeChecker):
        self.type_checker = type_checker

    def defined_in_attributes(self, attributes: dict, field: str, type_: Type) -> CheckerResult:
        defined_in_attributes = self.type_checker.exists_annotation(
            attributes, field)

        attr_type_check = self.type_checker.attr_has_same_type(
            attributes,
            field,
            type_
        )

        return CheckerResult(
            is_defined=defined_in_attributes,
            has_same_type=attr_type_check.has_same_type,
            existent_type=attr_type_check.existent_type
        )

    def defined_in_class(self, class_: Type, field: str, type_: Type) -> CheckerResult:
        members = inspect.getmembers(
            class_,
            lambda member: type(member) is dict and field in member
        )

        if len(members) > 0:
            member_attributes = members[0][1]

            member_type_check = self.type_checker.member_has_same_type(
                member_attributes,
                field,
                type_
            )

            return CheckerResult(
                is_defined=True,
                has_same_type=member_type_check.has_same_type,
                existent_type=member_type_check.existent_type
            )

        return CheckerResult(
            is_defined=False,
            has_same_type=False,
            existent_type=None
        )

    def defined_in_bases(self, field: str, type_: Type, bases: Tuple[Type]) -> CheckerResult:
        if not bases:
            return CheckerResult(
                is_defined=False,
                has_same_type=False,
                existent_type=None
            )

        for base in bases:
            current_base_check_result = self.defined_in_class(
                base,
                field,
                type_
            )

            if current_base_check_result.is_defined:
                return current_base_check_result

            base_check_result = self.defined_in_bases(
                field,
                type_,
                base.__bases__
            )

            if base_check_result.is_defined:
                return base_check_result

        return CheckerResult(
            is_defined=False,
            has_same_type=False,
            existent_type=None
        )


DefinitionChecker = __DefinitionChecker(TypeChecker)
