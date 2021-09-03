from lusyringe import lusyringe

from .docs.health_docs import health_openapi


class HealthResponse(metaclass=lusyringe(health_openapi)):
    ping: str
