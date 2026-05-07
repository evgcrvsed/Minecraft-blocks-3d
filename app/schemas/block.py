from pydantic import BaseModel, ConfigDict, Field


class BlockBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Название блока"
    )
    minecraft_id: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="minecraft:stone или просто stone"
    )
    info: str | None = Field(None, description="Дополнительная информация")

class BlockCreate(BlockBase):
    pass

class BlockDelete(BaseModel):
    minecraft_id: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="minecraft:stone или просто stone"
    )

class BlockRead(BlockBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
