from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    WHATSAPP_TOKEN: str = ""

    class Config:
        env_file = ".env"

settings = Settings()