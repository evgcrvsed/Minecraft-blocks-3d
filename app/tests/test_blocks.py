import pytest
from schemas.block import BlockCreate, BlockDelete


@pytest.mark.asyncio
async def test_create_block_success(client):
    payload = {
        "name": "Алмазный блок",
        "minecraft_id": "diamond_block",
        "info": "Очень ценный блок"
    }
    response = await client.post("/blocks/create", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Алмазный блок"
    assert data["minecraft_id"] == "diamond_block"
    assert data["id"] is not None


@pytest.mark.asyncio
async def test_create_block_duplicate(client):
    # Сначала создаём
    payload = {"name": "Дуб", "minecraft_id": "oak_log"}
    await client.post("/blocks/create", json=payload)

    # Пытаемся создать второй раз
    response = await client.post("/blocks/create", json=payload)

    assert response.status_code == 409
    assert "уже существует" in response.json()["detail"]


@pytest.mark.asyncio
async def test_delete_block_success(client):
    # Создаём блок
    payload = {"name": "Камень", "minecraft_id": "stone"}
    await client.post("/blocks/create", json=payload)

    # Удаляем
    response = await client.delete("/blocks/stone")

    assert response.status_code == 204  # No Content — стандарт для DELETE


@pytest.mark.asyncio
async def test_delete_block_not_found(client):
    response = await client.delete("/blocks/non_existing_block")

    assert response.status_code == 404
    assert "не найден" in response.json()["detail"]


@pytest.mark.asyncio
async def test_delete_block_invalid_id(client):
    """Проверка валидации minecraft_id (Pydantic)"""
    response = await client.delete("/blocks/")  # пустой id
    assert response.status_code == 422  # FastAPI валидация path param