from syringe import syringe

from .docs.health_docs import health_openapi


class HealthResponse(metaclass=syringe(health_openapi)):
    ping: str
