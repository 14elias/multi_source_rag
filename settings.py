from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_API_BASE_URL: str
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str
    HUGGING_API_KEY: str

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()