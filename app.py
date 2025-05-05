from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess
import os
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

app = FastAPI()

MODEL_PATH = "artifacts/model_trainer/pegasus-samsum-model"
TOKENIZER_PATH = "artifacts/model_trainer/tokenizer"

# Input schema for inference
class TextInput(BaseModel):
    text: str

@app.post("/retrain")
def retrain_model():
    """
    Trigger the full retraining pipeline from main.py
    """
    try:
        subprocess.run(["python", "main.py"], check=True)
        return {"message": "Model retrained and artifacts saved successfully."}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error in retraining: {str(e)}")

@app.post("/summarize")
def summarize_text(input: TextInput):
    """
    Generate a summary using the fine-tuned Pegasus model.
    """
    if not os.path.exists(MODEL_PATH) or not os.path.exists(TOKENIZER_PATH):
        raise HTTPException(status_code=404, detail="Model or tokenizer not found. Retrain the model first.")

    try:
        tokenizer = PegasusTokenizer.from_pretrained(TOKENIZER_PATH)
        model = PegasusForConditionalGeneration.from_pretrained(MODEL_PATH)

        inputs = tokenizer(input.text, truncation=True, padding="longest", return_tensors="pt")
        summary_ids = model.generate(**inputs)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return {"summary": summary}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference failed: {str(e)}")
