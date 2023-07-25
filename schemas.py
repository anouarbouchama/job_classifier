from typing import Optional
from pydantic import BaseModel


class UserMessage(BaseModel):
    text: str
    model_name: Optional[str]