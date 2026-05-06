from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.block import BlockCreate, BlockRead
from repositories.block import BlockRepository
from db.session import get_db

router = APIRouter(prefix="/blocks", tags=["blocks"])


@router.post("/", response_model=BlockRead, status_code=201)
async def create_block(
    block_in: BlockCreate,
    db: AsyncSession = Depends(get_db)
):
    repo = BlockRepository(db)
    block = await repo.create(block_in)
    return block