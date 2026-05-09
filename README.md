# Minecraft Blocks 3D

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/compose/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Современный FastAPI-бэкенд** для работы с 3D-блоками в стиле Minecraft.  
Проект создан как демонстрация **профессионального уровня** backend-разработки: чистая архитектура, лучшие практики 2025–2026 годов, полная контейнеризация и готовность к продакшену.

## ✨ Возможности

- Полноценный **CRUD** для Minecraft-блоков (создание, чтение, обновление, удаление)
- Поддержка 3D-данных (координаты, текстуры, свойства блоков)
- Чистая, масштабируемая архитектура (Layered / Clean Architecture)
- Асинхронная обработка запросов
- Валидация данных через Pydantic v2
- Абстракция доступа к данным через репозитории
- Полная контейнеризация (Docker + Docker Compose)

## 🛠 Технологический стек

| Слой              | Технология                          | Версия / Примечание          |
|-------------------|-------------------------------------|------------------------------|
| Язык              | Python                              | 3.12+                        |
| Фреймворк         | FastAPI                             | последняя версия             |
| Валидация         | Pydantic                            | v2                           |
| ORM               | SQLAlchemy                          | 2.0 (async)                 |
| База данных       | PostgreSQL / SQLite (на выбор)      | через Docker                 |
| Контейнеризация   | Docker + Docker Compose             | multi-stage build            |
| Документация      | OpenAPI (Swagger + ReDoc)           | автоматически                |

## 🚀 Быстрый запуск

```bash
# 1. Клонируем репозиторий
git clone https://github.com/evgcrvsed/Minecraft-blocks-3d.git
cd Minecraft-blocks-3d

# 2. Запускаем через Docker Compose (рекомендуемый способ)
docker compose up --build
```
Приложение будет доступно по адресу: http://localhost:8000