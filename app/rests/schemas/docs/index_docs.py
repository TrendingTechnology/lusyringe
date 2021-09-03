from pydantic.fields import Field

from datetime import datetime, timezone

current_date = datetime.now(timezone.utc)

index_openapi = {
    'message': (str, Field(..., example='Hey Yo! Sean Kingston')),
    'timestamp': (str, Field(..., example=current_date))
}
