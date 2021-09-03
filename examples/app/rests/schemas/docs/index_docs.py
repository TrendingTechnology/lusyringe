from lusyringe import Prescription

from pydantic.fields import Field

from datetime import datetime, timezone

current_date = datetime.now(timezone.utc)


index_openapi = [
    Prescription(
        field='message',
        type=str,
        doc=Field(..., example='Hey Yo! Sean Kingston')
    ),
    Prescription(
        field='timestamp',
        type=str,
        doc=Field(..., example=current_date)
    )
]
