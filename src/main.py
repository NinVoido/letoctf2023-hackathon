from fastapi import FastAPI
from .routers import items, users  # Импортируем роутеры из пакета routers
from .internal import admin  # Импортируем модуль admin из пакета internal

app = FastAPI()

# Включаем роутеры
app.include_router(items.router)  # Включаем роутер items
app.include_router(users.router)  # Включаем роутер users
app.include_router(admin.router)  # Включаем роутер admin

# Дополнительная конфигурация приложения или эндпоинты
# ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=0000)