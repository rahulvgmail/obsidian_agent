from fastapi import FastAPI, HTTPException
from app.services.llama_service import LlamaService
from app.services.obsidian_service import ObsidianService
from app.services.vector_store_service import VectorStoreService
from app.config import settings

app = FastAPI()

try:
    llama_service = LlamaService(model_path=settings.llama_model_path)
    obsidian_service = ObsidianService(vault_path=settings.obsidian_vault_path)
    vector_store_service = VectorStoreService(persist_directory=settings.vector_store_path)
except RuntimeError as e:
    print(f"Failed to initialize services: {str(e)}")
    llama_service, obsidian_service, vector_store_service = None, None, None

@app.post("/initialize")
async def initialize():
    if not all([llama_service, obsidian_service, vector_store_service]):
        raise HTTPException(status_code=503, detail="Services are not available")
    notes = obsidian_service.read_notes()
    vector_store_service.add_documents(notes)
    return {"message": "Initialization complete"}

@app.post("/query")
async def query(query_text: str):
    if not all([llama_service, vector_store_service]):
        raise HTTPException(status_code=503, detail="Services are not available")
    results = vector_store_service.query(query_text)
    context = "\n".join(results['documents'][0])
    response = llama_service.generate_with_context(query_text, context)
    return {"response": response, "sources": results['metadatas'][0]}

@app.post("/update_note")
async def update_note(path: str, content: str):
    if not obsidian_service:
        raise HTTPException(status_code=503, detail="Obsidian service is not available")
    obsidian_service.update_note(path, content)
    return {"message": "Note updated successfully"}
