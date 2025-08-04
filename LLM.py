from llama_cpp import Llama
import os
import json

class LLM:
    def __init__(self, model_path="TomoBrain/Models/Phi-3-mini-4k-instruct-q4.gguf"):
        os.makedirs("TomoBrain/Models", exist_ok=True)
        self.chat_history_path = os.path.join("TomoBrain", "Models", "chat_history_notes.json")

        # 🔄 Use a larger context window for longer prompt+response
        print(f"[INFO] Loading LLaMA model from {model_path} ...")
        self.llm = Llama(model_path=model_path, n_ctx=2048)  # ← CHANGED!
        print("[INFO] LLaMA model loaded!")

    def query_llama_streaming_recommendation(self, prompt, save_dir=None, progress_label=None):
        print(f" Sending to LLaMA for recommendation: {prompt}\n LLaMA says:")
        recom_history_path = os.path.join("TomoBrain", "Models", "chat_history_recom.json")
        try:
            with open(recom_history_path, "r", encoding="utf-8", errors="ignore") as f:
                chat_history = json.load(f)
        except FileNotFoundError:
            chat_history = []

        full_prompt = ""
        for msg in chat_history:
            if msg["role"] == "system":
                full_prompt += f"<|system|>{msg['content']}"
            elif msg["role"] == "user":
                full_prompt += f"<|user|>{msg['content']}"
            else:
                full_prompt += f"<|assistant|>{msg['content']}"
        full_prompt += f"<|user|>{prompt}<|assistant|>"

        buffer = ""
        llmResponse = ""

        # 🔄 Use larger max_tokens and optional sampling params
        for output in self.llm(full_prompt, max_tokens=512, temperature=0.7, top_p=0.9, stream=True):  # ← CHANGED!
            content = output["choices"][0]["text"]
            print(content, end='', flush=True)
            buffer += content
            llmResponse += content

        print("\n Finished speaking.\n\n")
        print(llmResponse.strip())

        if save_dir is not None:
            os.makedirs(save_dir, exist_ok=True)
            rec_path = os.path.join(save_dir, "UserRecommendation.txt")
            with open(rec_path, "w", encoding="utf-8") as f:
                f.write(llmResponse.strip())

    def query_llama_streaming_journal(self, prompt, save_dir=None, progress_label=None):
        print(f" Sending to LLaMA: {prompt}\n LLaMA says:")

        try:
            with open(self.chat_history_path, "r", encoding="utf-8", errors="ignore") as f:
                chat_history = json.load(f)
        except FileNotFoundError:
            chat_history = []

        full_prompt = ""
        for msg in chat_history:
            if msg["role"] == "system":
                full_prompt += f"<|system|>{msg['content']}"
            elif msg["role"] == "user":
                full_prompt += f"<|user|>{msg['content']}"
            else:
                full_prompt += f"<|assistant|>{msg['content']}"
        full_prompt += f"<|user|>{prompt}<|assistant|>"

        buffer = ""
        llmResponse = ""

        # 🔄 Use larger max_tokens and optional sampling params
        for output in self.llm(full_prompt, max_tokens=512, temperature=0.7, top_p=0.9, stream=True):  # ← CHANGED!
            content = output["choices"][0]["text"]
            print(content, end='', flush=True)
            buffer += content
            llmResponse += content

        print("\n Finished speaking.\n\n")
        print(llmResponse.strip())

        if save_dir is not None:
            os.makedirs(save_dir, exist_ok=True)
            rec_path = os.path.join(save_dir, "LLMRecommendation.txt")
            with open(rec_path, "w", encoding="utf-8") as f:
                f.write(llmResponse.strip())
        return llmResponse.strip()
