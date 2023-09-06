from os import makedirs
from uuid import UUID

from blacksheep import Application, Request, Response, bad_request, created
from src.handlers import RoomHandler
from src.models import Image, ImageData, Room

makedirs("media", exist_ok=True)

app = Application()
app.serve_files("media", root_path="media")
app.use_cors(
    allow_methods="*",
    allow_origins="*",
    allow_headers="* Authorization",
    max_age=300,
)
router = app.router

room_handler = RoomHandler()


@router.post("/api/room")
async def create_room() -> Response:
    room = await room_handler.create()
    return created(room.id.hex)


@router.get("/api/room/{room_id}")
async def get_room(room_id: UUID) -> Room:
    return await room_handler.get_by_id(room_id)


@router.post("/api/room/{room_id}/upload")
async def upload(request: Request, room_id: UUID) -> Response:
    files = await request.files()

    if not files:
        return bad_request("Missing images.")

    for file in files:
        image = ImageData(name=file.file_name.decode(), bytes=file.data)
        await room_handler.upload(room_id, image)

    return created()
