from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.block import BlockCreate, BlockRead
from db.session import get_db
from services.block import BlockService

router = APIRouter(prefix="/blocks", tags=["Blocks"])


@router.post("/", response_model=BlockRead, status_code=201)
async def create_block(
    block_in: BlockCreate,
    db: AsyncSession = Depends(get_db),
    service: AsyncSession = Depends(get_db),
):
    return await service.create_block(block_in)
