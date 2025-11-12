from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os, runpod

app = FastAPI()

# 🗝️ קריאת המפתח מהסביבה
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY")
runpod.api_key = RUNPOD_API_KEY

# 🟢 החזרת יתרה נוכחית מרנפוד
@app.get("/balance")
def get_balance():
    """
    מחזיר את היתרה הקיימת בחשבון RunPod שלך.
    """
    try:
        balance = runpod.get_balance()
        return JSONResponse({"balance": balance.get("balance", 0.0)})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
