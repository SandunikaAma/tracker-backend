from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models.shipment import Shipment
from routes import shipments
from routes.shipments import router as shipment_router

app = FastAPI()

# Enable CORS for frontend communication

origins = ["http://localhost:3000", "https://tracker-app.vercel.app"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoints

@app.get("/api/shipments", response_model=List[Shipment])
async def get_shipments():
    return shipments

@app.get("/api/shipments/metrics")
async def get_metrics():
    # Calculate shipment metrics
    total = len(shipments)
    fedex_count = sum(1 for shipment in shipments if shipment["carrier"] == "FedEx")
    dhl_count = sum(1 for shipment in shipments if shipment["carrier"] == "DHL")
    in_progress = sum(1 for shipment in shipments if shipment["status"] == "in-progress")
    delivered = sum(1 for shipment in shipments if shipment["status"] == "delivered")

    return {
        "totalShipments": total,
        "fedexShipments": fedex_count,
        "dhlShipments": dhl_count,
        "inProgress": in_progress,
        "delivered": delivered,
    }

@app.post("/api/shipments", response_model=Shipment)
async def create_shipment(shipment: Shipment):
    shipments.append(shipment.dict())  # Add new shipment to database
    return shipment