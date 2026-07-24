import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. نوصل لفولدر mini-rag-app الأساسي
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 2. نربط المسار مباشرة بملف .env
ENV_PATH = os.path.join(BASE_DIR, ".env")

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    
    # تعديل أسماء المتغيرات لـ Uppercase لتطابق DataController
    FILE_ALLOWED_TYPES: list = ["application/pdf", "text/plain"]
    FILE_MAX_SIZE: int = 10  # بالـ Megabytes مثلاً
    FILE_DEFAULT_CHUNK_SIZE: int = 512

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )

def get_settings():
    return Settings()