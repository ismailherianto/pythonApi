from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    app_env: str = "development"
    debug: bool = True
    api_key: str = "default"
    app_host: str
    app_port: int

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
