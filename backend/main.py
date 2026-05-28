from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

app = FastAPI()

# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class CodeRequest(BaseModel):
    code: str

# Home route
@app.get("/")
def home():
    return {"message": "Backend works!"}

# AI explain route
@app.post("/explain")
def explain_code(request: CodeRequest):

    prompt = f"""
Explain this code in plain English.

Include:
1. Overall summary
2. Line-by-line explanation
3. Time complexity
4. Space complexity

Code:
{request.code}
"""

    response = model.generate_content(prompt)

    return {
        "explanation": response.text
    }