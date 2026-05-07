from sqlalchemy.ext.asyncio import AsyncSession
from repositories.block import BlockRepository
from schemas.block import BlockCreate, BlockDelete, BlockRead
from fastapi import HTTPException, status


class BlockService:
    def __init__(self, db: AsyncSession):
        self.repo = BlockRepository(db)

    async def create_block(self, block_in: BlockCreate) -> BlockRead:
        # Бизнес-логика
        existing = await self.repo.get_by_minecraft_id(block_in.minecraft_id)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Блок с таким minecraft_id уже существует"
            )

        # Дополнительная валидация/обработка
        if not block_in.name.strip():
            raise HTTPException(status_code=400, detail="Имя блока не может быть пустым")

        block = await self.repo.create(block_in)
        return BlockRead.model_validate(block)


    async def delete_block(self, block_in: BlockDelete) -> BlockRead:
        # Проверка существования
        existing = await self.repo.get_by_minecraft_id(block_in.minecraft_id)
        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Блок с minecraft_id '{block_in.minecraft_id}' не найден"
            )

        deleted_block = await self.repo.delete(block_in.minecraft_id)
        if not deleted_block:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Блок не найден при удалении"
            )

        return BlockRead.model_validate(deleted_block)


