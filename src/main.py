from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import base, data
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- [بداية التشغيل - Startup] ---
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    
    await init_beanie(
        database=app.db_client,
        document_models=[
            # ضيف الـ Document Models هنا لما تكريتها
        ]
    )
    
    yield  # التطبيق بيفضل شغال هنا
    
    # --- [عند الإغلاق - Shutdown] ---
    app.mongo_conn.close()


# بنمرر الـ lifespan للتطبيق مباشرة
app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)