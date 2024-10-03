import llama_cpp

class LlamaService:
    def __init__(self, model_path):
        try:
            self.llm = llama_cpp.Llama(model_path=model_path)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Llama model: {str(e)}")

    def chat(self, prompt):
        try:
            response = self.llm(prompt, max_tokens=100)
            return response['choices'][0]['text']
        except Exception as e:
            return f"Error in chat: {str(e)}"

    def review_file(self, file_content):
        prompt = f"Please review the following file content:\n\n{file_content}\n\nProvide a summary and any potential issues:"
        return self.chat(prompt)
