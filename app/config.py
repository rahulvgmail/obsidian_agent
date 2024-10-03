from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llama_model_path: str = "path/to/your/llama/model.bin"

settings = Settings()
