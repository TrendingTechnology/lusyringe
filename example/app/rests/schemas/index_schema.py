from lusyringe import lusyringe

from .docs.index_docs import index_openapi


class Message:
    message: str


class Time:
    timestamp: str


class Timestamp(Time, Message):
    pass


class IndexResponse(Timestamp, metaclass=lusyringe(index_openapi)):
    pass
