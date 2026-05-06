from .base import BaseRepository
from models.block import Block
from schemas.block import BlockCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BlockRepository(BaseRepository[Block]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Block)

    async def create(self, block_in: BlockCreate) -> Block:
        db_block = Block(**block_in.model_dump())
        self.session.add(db_block)
        await self.session.commit()
        await self.session.refresh(db_block)
        return db_block