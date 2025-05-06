from typing import Literal, Union
from pydantic import BaseModel

from models import generate_optional

@generate_optional()
class User(BaseModel):
    first_name: Union[str, Literal["Alessandro"]]
    last_name: str
