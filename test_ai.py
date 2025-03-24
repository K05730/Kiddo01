import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "C:/Users/kris/AI_Models/mistralai/Mistral-7B-Instruct-v0.1"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_path)

inputs = tokenizer("make add (a, b):", return_tensors="pt")

output = model.generate(**inputs, max_new_tokens=50, do_sample=True)

print(tokenizer.decode(output[0], skip_special_tokens=True))
