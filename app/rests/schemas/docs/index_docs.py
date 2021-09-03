from pydantic.fields import Field

from datetime import datetime, timezone

current_date = datetime.now(timezone.utc)

index_openapi = {
    'message': Field(..., example='Hey Yo! Sean Kingston'),
    'timestamp': Field(..., example=current_date)
}
