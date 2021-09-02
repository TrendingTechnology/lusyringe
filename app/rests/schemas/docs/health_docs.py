from pydantic.fields import FieldInfo


health_openapi = {
    'ping': FieldInfo(..., example='Ponguinho =)')
}
