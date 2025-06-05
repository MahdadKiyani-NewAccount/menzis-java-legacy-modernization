from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

parked_vehicles = {}

class CheckInRequest(BaseModel):
    license_plate: str
    zone_id: str

class CheckOutRequest(BaseModel):
    license_plate: str

@app.post("/check-in")
def check_in(req: CheckInRequest):
    if req.license_plate in parked_vehicles:
        raise HTTPException(status_code=400, detail="Already parked")
    parked_vehicles[req.license_plate] = req.zone_id
    return {"message": "Vehicle checked in", "zone": req.zone_id}

@app.post("/check-out")
def check_out(req: CheckOutRequest):
    if req.license_plate not in parked_vehicles:
        raise HTTPException(status_code=404, detail="Not found")
    del parked_vehicles[req.license_plate]
    return {"message": "Checked out"}

