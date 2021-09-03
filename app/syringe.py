from pydantic import BaseModel as __BaseModel__


class __Meta__(type):
    __doc_fields: dict
    __doc_strict: bool

    def __new__(self, class_name, bases, attributes: dict):
        if '__annotations__' in attributes:
            if not self.__doc_strict:
                __Meta__.__apply_loose_attrs(self.__doc_fields, attributes)
            else:
                __Meta__.__apply_strict_attrs(self.__doc_fields,
                                              attributes, class_name)
        elif self.__doc_strict:
            raise NotImplementedError(
                f'No attribute implemented in {class_name}, expected {list(self.__doc_fields.keys())}')

        return type(class_name, (__BaseModel__, *bases), attributes)

    def __setdoc__(self, fields, strict):
        self.__doc_fields = fields
        self.__doc_strict = strict

    def __apply_loose_attrs(fields, attributes):
        for field in attributes['__annotations__']:
            if value := fields.get(field):
                attributes[field] = value

    def __apply_strict_attrs(fields, attributes, class_name):
        for field, value in fields.items():
            if not field in attributes['__annotations__']:
                raise NotImplementedError(
                    f'Documentation for {field} was found, but field was not implemented in {class_name}')

            attributes[field] = value


def syringe(doc_spec, strict=True):
    class MetaClass(__Meta__):
        pass

    MetaClass.__setdoc__(MetaClass, doc_spec, strict)

    return MetaClass
