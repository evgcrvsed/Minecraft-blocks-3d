from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from services.block import BlockService


def get_block_service(db: AsyncSession = Depends(get_db)) -> BlockService:
    return BlockService(db)