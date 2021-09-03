from pydantic.fields import Field


health_openapi = {
    'ping': (str, Field(..., example='Pong =D'))
}
