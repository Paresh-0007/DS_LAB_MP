
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

from huggingface_hub import login

login("paste your hugginggace token")  # 🔒 Replace with your actual token (keep it private!)

# Download full base model to local dir
base_dir = "./models/mistral-base"
tokenizer_dir = "./models/mistral-tokenizer"

# Downloads all model files
snapshot_download("mistralai/Mistral-7B-v0.1", local_dir=base_dir)

# Also download tokenizer manually if needed
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
tokenizer.save_pretrained(tokenizer_dir)
