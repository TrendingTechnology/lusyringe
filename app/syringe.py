from typing import Tuple, Type
from pydantic import BaseModel as __BaseModel__

import inspect


class __Meta__(type):
    __doc_fields: dict
    __doc_strict: bool

    def __new__(self, class_name, bases, attributes: dict):
        if not '__annotations__' in attributes:
            attributes['__annotations__'] = {}

        if self.__doc_strict:
            __Meta__.__apply_strict_attrs(self.__doc_fields,
                                          attributes, bases, class_name)
        else:
            __Meta__.__apply_loose_attrs(self.__doc_fields, attributes)

        return type(class_name, (__BaseModel__, *bases), attributes)

    def __setdoc__(self, fields, strict):
        self.__doc_fields = fields
        self.__doc_strict = strict

    def __apply_loose_attrs(fields, attributes):
        for field, spec in fields.items():
            attributes["__annotations__"][field] = spec[0]
            attributes[field] = spec[1]

    def __apply_strict_attrs(fields, attributes, bases, class_name):
        for field, spec in fields.items():
            if not field in attributes['__annotations__'] and not __Meta__.__defined_in_bases(field, bases):
                raise NotImplementedError(
                    f'Documentation for {field} was found, but field was not implemented in {class_name}')

            attributes["__annotations__"][field] = spec[0]
            attributes[field] = spec[1]

    def __defined_in_bases(field: str, bases: Tuple[Type]):
        if not bases:
            return False

        found = False

        for base in bases:
            members = inspect.getmembers(
                base,
                lambda member: type(member) is dict and field in member
            )

            if len(members) > 0:
                return True
            else:
                found = __Meta__.__defined_in_bases(
                    field, base.__bases__)

            if found == True:
                return True

        return False


def syringe(doc_spec, strict=True):
    class MetaClass(__Meta__):
        pass

    MetaClass.__setdoc__(MetaClass, doc_spec, strict)

    return MetaClass
