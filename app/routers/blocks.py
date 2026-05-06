from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.block import BlockCreate, BlockRead
from repositories.block import BlockRepository
from db.session import get_db

router = APIRouter(prefix="/blocks", tags=["Blocks"])


@router.post("/", response_model=BlockRead, status_code=201)
async def create_block(
    block_in: BlockCreate,
    db: AsyncSession = Depends(get_db)
):
    repo = BlockRepository(db)
    block = await repo.get_by_minecraft_id(block_in.minecraft_id)
    if block:
        raise HTTPException(status_code=409, detail="Блок с таким id уже существует!")
    return await repo.create(block_in)
