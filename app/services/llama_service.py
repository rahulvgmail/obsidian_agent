import llama_cpp

class LlamaService:
    def __init__(self, model_path):
        self.llm = llama_cpp.Llama(model_path=model_path)

    def chat(self, prompt):
        response = self.llm(prompt, max_tokens=100)
        return response['choices'][0]['text']

    def review_file(self, file_content):
        prompt = f"Please review the following file content:\n\n{file_content}\n\nProvide a summary and any potential issues:"
        return self.chat(prompt)
