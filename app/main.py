from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI(title="k-station-ai",version="0.3.0")
class Query(BaseModel): query:str
@app.get("/health")
def health(): return {"status":"ok","project":"k-station-ai","version":"0.3.0"}
@app.post("/analyze")
def analyze(req:Query): return {"domain":"station-area","query":req.query,"checks":["500m/1km/2km","land/buildings","mobility","development constraints"],"status":"prototype"}
