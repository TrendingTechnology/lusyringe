from pydantic.fields import Field


from syringe.data import Prescription

health_openapi = [
    Prescription(
        field='ping',
        type=str,
        doc=Field(..., example='Pong')
    )
]
