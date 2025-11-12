from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os, requests

app = FastAPI()

RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY")

@app.get("/balance")
def get_balance():
    """מחזיר את היתרה הנוכחית מחשבון ה-RunPod שלך."""
    try:
        headers = {"Authorization": f"Bearer {RUNPOD_API_KEY}"}
        url = "https://api.runpod.ai/v2/user/balance"
        response = requests.get(url, headers=headers)
        data = response.json()
        return JSONResponse(data)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
