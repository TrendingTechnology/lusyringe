from typing import List, Tuple, Type
from pydantic import BaseModel as __BaseModel__


from .checkers import DefinitionChecker

from .data import Prescription

from .errors import LuSyringeError


class __Meta__(type):
    __doc_fields: dict
    __doc_strict: bool

    def __new__(self, class_name, bases, attributes: dict):
        if not '__annotations__' in attributes:
            attributes['__annotations__'] = {}

        if self.__doc_strict:
            __Meta__.__apply_strict_attrs(
                self.__doc_fields,
                attributes,
                bases,
                class_name
            )
        else:
            __Meta__.__apply_loose_attrs(
                self.__doc_fields,
                attributes,
                bases,
                class_name
            )

        return type(
            class_name,
            (__BaseModel__, *bases),
            attributes
        )

    def __setdoc__(self, fields, strict):
        self.__doc_fields = fields
        self.__doc_strict = strict

    def __inject__(attributes: dict, prescription: Prescription):
        type_annotations = attributes["__annotations__"]

        type_annotations[prescription.field] = prescription.type
        attributes[prescription.field] = prescription.doc

    def __apply_loose_attrs(prescriptions: List[Prescription], attributes: dict, bases: Tuple[Type], class_name: str):
        for prescription in prescriptions:
            attribute_check_result = DefinitionChecker.defined_in_attributes(
                attributes,
                prescription.field,
                prescription.type
            )

            if attribute_check_result.is_defined and not attribute_check_result.has_same_type:
                raise LuSyringeError.illegal_type_attribution(
                    class_name,
                    prescription.field,
                    prescription.type,
                    attribute_check_result.existent_type
                )

            base_check_result = DefinitionChecker.defined_in_bases(
                prescription.field,
                prescription.type,
                bases
            )

            if base_check_result.is_defined and not base_check_result.has_same_type:
                raise LuSyringeError.illegal_type_attribution(
                    class_name,
                    prescription.field,
                    prescription.type,
                    base_check_result.existent_type
                )

            __Meta__.__inject__(attributes, prescription)

    def __apply_strict_attrs(prescriptions: List[Prescription], attributes: dict, bases: Tuple[Type], class_name: str):
        for prescription in prescriptions:
            attribute_check_result = DefinitionChecker.defined_in_attributes(
                attributes,
                prescription.field,
                prescription.type
            )

            if attribute_check_result.is_defined:
                if attribute_check_result.has_same_type:
                    __Meta__.__inject__(attributes, prescription)

                    return
                else:
                    raise LuSyringeError.illegal_type_attribution(
                        class_name,
                        prescription.field,
                        prescription.type,
                        attribute_check_result.existent_type
                    )

            base_check_result = DefinitionChecker.defined_in_bases(
                prescription.field,
                prescription.type,
                bases
            )

            if not base_check_result.is_defined:
                raise LuSyringeError.attribute_not_implemented(
                    class_name,
                    prescription.field,
                    prescription.type
                )
            elif not base_check_result.has_same_type:
                raise LuSyringeError.illegal_type_attribution(
                    class_name,
                    prescription.field,
                    prescription.type,
                    base_check_result.existent_type
                )

            __Meta__.__inject__(attributes, prescription)


def lusyringe(doc_spec: List[Prescription], strict=True):
    class MetaClass(__Meta__):
        pass

    MetaClass.__setdoc__(MetaClass, doc_spec, strict)

    return MetaClass
