from pydantic import BaseModel

class Settings(BaseModel):
    llama_model_path: str = "path/to/your/llama/model.bin"
    obsidian_vault_path: str = "path/to/your/obsidian/vault"
    vector_store_path: str = "path/to/vector/store"

settings = Settings()
