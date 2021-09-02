from doccer import doccer

from .docs.health_docs import health_openapi


class HealthResponse(metaclass=doccer(health_openapi)):
    ping: str
