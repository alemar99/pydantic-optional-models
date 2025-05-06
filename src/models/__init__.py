from typing import TypeVar
from pydantic import BaseModel

class Unset(BaseModel):
    """Sentinel object"""

    def __eq__(self, other):
        return other.__class__ is self.__class__

    def __repr__(self):
        return "Unset"


UNSET = Unset()


T = TypeVar("T")

def generate_optional():
    def decorate(cls: type[T]) -> type[T]:
        setattr(cls, "__generate_optional__", True)
        return cls

    return decorate

FieldType = TypeVar("FieldType")

class BasePartial(BaseModel):
    """Base class for all the partial models.

    You can use it to add your own common methods.
    """
    def safe_get(self, field: FieldType | Unset) -> FieldType:
        """Safely access a field.
        
        Will raise a reference error if you try to access a field that is Unset.
        """
        if isinstance(field, Unset):
            raise ReferenceError("The field you tried to access is Unset.")
        return field

