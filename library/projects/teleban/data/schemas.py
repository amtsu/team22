from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Subscription(BaseModel):
    user_id: int
    source: str
    tag: str

    model_config = ConfigDict(from_attributes=True)


class Content(BaseModel):
    link: str
    title: str
    source: str
    tags: list[str]
    date_time: datetime = datetime.now()
    status: bool
    text: str | None = None
    translation: str | None = None

    model_config = ConfigDict(from_attributes=True)

