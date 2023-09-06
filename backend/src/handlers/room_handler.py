from uuid import UUID

from injection import inject
from src.models import ImageData, Room

from src.repositories import RoomRepository


class RoomHandler:
    @inject
    def __init__(self, room_repository: RoomRepository):
        self.room_repository = room_repository

    async def create(self) -> Room:
        room = Room()
        await self.room_repository.add(room)
        return room

    async def get_by_id(self, room_id: UUID) -> Room:
        return await self.room_repository.get_by_id(room_id)

    async def upload(self, room_id: UUID, data: ImageData):
        await self.room_repository.upload(room_id, data)
