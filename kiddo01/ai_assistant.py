import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os

class Kiddo01AIAssistant:
    def __init__(self):
        print("🔹 Loading local AI model (TinyLlama-1.1B)...")
        self.model = AutoModelForCausalLM.from_pretrained(
            "C:/Users/kris/AI_Models/TinyLlama-1.1B",
            torch_dtype=torch.float32,
            device_map="cpu"
        )
        self.tokenizer = AutoTokenizer.from_pretrained("C:/Users/kris/AI_Models/TinyLlama-1.1B")
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def suggest_code(self, user_input):
        print("🔹 Generating suggestion using local model...")
        result = self.generator(f"Kiddo01 code: {user_input}\nNext line:", max_length=50, do_sample=True)[0]['generated_text']
        print("💡 AI Suggestion:", result)
