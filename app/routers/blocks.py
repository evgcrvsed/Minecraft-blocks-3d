from fastapi import APIRouter, Depends
from schemas.block import BlockCreate, BlockRead, BlockDelete

from routers.dependencies import get_block_service   # ← импорт
from services.block import BlockService

router = APIRouter(prefix="/blocks", tags=["Blocks"])


@router.post("/create", response_model=BlockRead, status_code=201)
async def create_block(
    block_in: BlockCreate,
    service: BlockService = Depends(get_block_service)   # ← правильно!
):
    return await service.create_block(block_in)

@router.post("/delete", response_model=BlockRead, status_code=201)
async def delete_block(
    block_in: BlockDelete,
    service: BlockService = Depends(get_block_service)   # ← правильно!
):
    return await service.delete_block(block_in)