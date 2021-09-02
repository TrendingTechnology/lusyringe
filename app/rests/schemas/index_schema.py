from doccer import doccer

from .docs.index_docs import index_openapi


class IndexResponse(metaclass=doccer(index_openapi)):
    message: str
