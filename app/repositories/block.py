from .base import BaseRepository
from models.block import Block
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class BlockRepository(BaseRepository[Block]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Block)

    # async def get_by_name(
    #         self,
    #         owner_id: int,
    #         completed: bool | None = None
    # ):
    #     stmt = select(Todo).where(Todo.owner_id == owner_id)
    #
    #     if completed is not None:
    #         stmt = stmt.where(Todo.completed == completed)
    #
    #     result = await self.session.execute(stmt)
    #     return list(result.scalars().all())
    #
    # async def get_by_completed(self, completed: bool | None = None):
    #     stmt = select(Todo)
    #     if completed is not None:
    #         stmt = stmt.where(Todo.completed == completed)
    #     result = await self.session.execute(stmt)
    #     return list(result.scalars().all())