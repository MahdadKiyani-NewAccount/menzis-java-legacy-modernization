from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/digid-login")
def digid_login():
    return RedirectResponse(url="/digid-verify")

@app.get("/digid-verify")
def digid_verify():
    return {"status": "verified", "user_id": "123456789"}

