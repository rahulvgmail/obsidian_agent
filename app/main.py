from fastapi import FastAPI, HTTPException
from app.services.llama_service import LlamaService
from app.config import settings

app = FastAPI()

try:
    llama_service = LlamaService(model_path=settings.llama_model_path)
except RuntimeError as e:
    print(f"Failed to initialize LlamaService: {str(e)}")
    llama_service = None

@app.post("/chat")
async def chat(prompt: str):
    if llama_service is None:
        raise HTTPException(status_code=503, detail="Llama service is not available")
    response = llama_service.chat(prompt)
    return {"response": response}

@app.post("/review_file")
async def review_file(file_content: str):
    if llama_service is None:
        raise HTTPException(status_code=503, detail="Llama service is not available")
    review = llama_service.review_file(file_content)
    return {"review": review}
