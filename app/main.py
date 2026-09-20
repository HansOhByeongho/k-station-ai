from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title="K-Station AI",version="0.1.0")
class Query(BaseModel):
    query:str

@app.get("/health")
def health(): return {"status":"ok","project":"k-station-ai","version":"0.1.0"}

@app.post("/analyze")
def analyze(req:Query):
    return {"project":"k-station-ai","domain":"station","query":req.query,"status":"prototype","next":"connect verified official data sources"}
