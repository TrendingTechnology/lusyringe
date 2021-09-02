from pydantic import BaseModel


class Meta(type):
    fields: dict

    def __new__(self, class_name, bases, attributes):

        if not '__annotations__' in attributes:
            return type(class_name, (BaseModel, *bases), attributes)

        for field in attributes['__annotations__']:
            if value := self.fields.get(field):
                attributes[field] = value

        return type(class_name, (BaseModel, *bases), attributes)


def doccer(config):
    class MetaClass(Meta):
        pass

    setattr(MetaClass, 'fields', config)

    return MetaClass
