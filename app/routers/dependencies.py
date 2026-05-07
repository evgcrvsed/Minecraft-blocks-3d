from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from services.block import BlockService
from db.session import get_db

async def get_block_service(db: AsyncSession = Depends(get_db)) -> BlockService:
    return BlockService(db)
