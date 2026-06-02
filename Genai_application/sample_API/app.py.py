from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# FastAPI app
app = FastAPI()

# Gemini Client
client = genai.Client(
     api_key="AQ.Ab8RN6KTorym3rhQDW4SbvlRLKEf-Qx_Rjysk7o3T8GZkYt-jA"
)

# Request Model
class Question(BaseModel):
    question: str

# Home API
@app.get("/")
def home():
    return {"message": "Gemini FastAPI Running Successfully"}

# Gemini API
@app.post("/ask")
def ask_gemini(data: Question):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data.question
        )

        return {
            "question": data.question,
            "answer": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }
