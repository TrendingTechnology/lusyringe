from typing import Type


class __TypeChecker:
    def __get_annotations(self, attributes: dict) -> dict:
        return attributes['__annotations__']

    def exists_annotation(self, attributes: dict, field: str) -> bool:
        return field in self.__get_annotations(attributes)

    def attr_has_same_type(self, attributes: dict, field: str, type_: Type) -> bool:
        if self.exists_annotation(attributes, field):
            return self.__get_annotations(attributes)[field] == type_

        return False

    def member_has_same_type(self, member: dict, field: str, type_: Type):
        return member[field] == type_


TypeChecker = __TypeChecker()
