from sqlalchemy import Text, String
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Block(Base):
    __tablename__ = "blocks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)  # "Камень"

    minecraft_id: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
        index=True
    )

    info: Mapped[str | None] = mapped_column(Text, nullable=True)
