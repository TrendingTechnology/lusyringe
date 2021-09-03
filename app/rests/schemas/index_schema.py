from syringe import syringe

from .docs.index_docs import index_openapi


class IndexResponse(metaclass=syringe(index_openapi)):
    message: str
    timestamp: str
