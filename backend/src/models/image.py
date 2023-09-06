from dataclasses import dataclass, field
from typing import Any
from uuid import UUID, uuid4


@dataclass(kw_only=True, slots=True)
class ImageData:
    name: str
    bytes: bytes


@dataclass(kw_only=True, slots=True)
class Image:
    id: UUID = field(default_factory=uuid4)
    name: str

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and other.id == self.id

    def __hash__(self) -> int:
        return id(self)
