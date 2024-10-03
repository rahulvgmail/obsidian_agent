from fastapi import FastAPI
from app.services.llama_service import LlamaService
from app.config import settings

app = FastAPI()
llama_service = LlamaService(model_path=settings.llama_model_path)

@app.post("/chat")
async def chat(prompt: str):
    response = llama_service.chat(prompt)
    return {"response": response}

@app.post("/review_file")
async def review_file(file_content: str):
    review = llama_service.review_file(file_content)
    return {"review": review}
