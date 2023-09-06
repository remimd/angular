from dataclasses import dataclass, field
from typing import Any
from uuid import UUID, uuid4

from src.models import Image


@dataclass(kw_only=True, slots=True)
class Room:
    id: UUID = field(default_factory=uuid4)
    images: list[Image] = field(default_factory=list)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and other.id == self.id

    def __hash__(self) -> int:
        return id(self)
