from fastapi import FastAPI
from pydantic import BaseModel
from google import genai

# ================= APP =================
app = FastAPI()

# ================= GEMINI CLIENT =================
client = genai.Client(
    api_key="AQ.Ab8RN6KTorym3rhQDW4SbvlRLKEf-Qx_Rjysk7o3T8GZkYt-jA"
)

# ================= REQUEST MODEL =================
class Question(BaseModel):
    question: str

# ================= HOME API =================
@app.get("/")
def home():
    return {"message": "Gemini FastAPI Running Successfully"}

# ================= GEMINI API =================
@app.post("/ask")
def ask_gemini(data: Question):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=data.question
    )

    return {
        "question": data.question,
        "answer": response.text
    }
