import llama_cpp

class LlamaService:
    def __init__(self, model_path):
        try:
            self.llm = llama_cpp.Llama(model_path=model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Llama model: {str(e)}")

    def generate(self, prompt, max_tokens=100):
        try:
            response = self.llm(prompt, max_tokens=max_tokens)
            return response['choices'][0]['text']
        except Exception as e:
            return f"Error in generation: {str(e)}"

    def generate_with_context(self, query, context, max_tokens=100):
        prompt = f"Context:\n{context}\n\nQuery: {query}\n\nResponse:"
        return self.generate(prompt, max_tokens)
