<<<<<<< HEAD
from typing import Optional
from pydantic import BaseModel


class UserMessage(BaseModel):
    text: str
=======
from typing import Optional
from pydantic import BaseModel


class UserMessage(BaseModel):
    text: str
>>>>>>> 4e51cdc74899f94428c5fe5c2ae69424b4e3983d
    model_name: Optional[str]