from os import makedirs
from os.path import dirname
from pathlib import Path
from uuid import UUID, uuid4

from blacksheep.exceptions import NotFound
from injection import unique
from src.models import Image, ImageData, Room


@unique
class RoomRepository:
    def __init__(self):
        self.data = set()

    async def add(self, room: Room) -> Room:
        self.data.add(room)
        return room

    async def get_by_id(self, room_id: UUID) -> Room:
        for room in self.data:
            if room_id == room.id:
                return room

        raise NotFound()

    async def upload(self, room_id: UUID, data: ImageData) -> Room:
        room = await self.get_by_id(room_id)

        directory = Path(f"media/{room_id.hex}")
        extension = data.name.rsplit(".", 1)[1]
        filename = f"{uuid4().hex}.{extension}"
        makedirs(directory, exist_ok=True)

        with open(directory / filename, "wb") as file:
            file.write(data.bytes)

        image = Image(name=filename)
        room.images.append(image)

        return room
