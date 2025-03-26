from fastapi import APIRouter, HTTPException
from models.shipment import Shipment
from typing import List

router = APIRouter()

# In-memory store for shipments
shipments_db = []

@router.post("/", response_model=Shipment)
def create_shipment(shipment: Shipment):
    shipments_db.append(shipment)
    return shipment

@router.get("/", response_model=List[Shipment])
def get_shipments():
    return shipments_db

@router.get("/{shipment_id}", response_model=Shipment)
def get_shipment(shipment_id: int):
    for shipment in shipments_db:
        if shipment.id == shipment_id:
            return shipment
    raise HTTPException(status_code=404, detail="Shipment not found")

@router.put("/{shipment_id}", response_model=Shipment)
def update_shipment(shipment_id: int, updated_shipment: Shipment):
    for index, shipment in enumerate(shipments_db):
        if shipment.id == shipment_id:
            shipments_db[index] = updated_shipment
            return updated_shipment
    raise HTTPException(status_code=404, detail="Shipment not found")

@router.delete("/{shipment_id}")
def delete_shipment(shipment_id: int):
    global shipments_db
    shipments_db = [shipment for shipment in shipments_db if shipment.id != shipment_id]
    return {"message": "Shipment deleted successfully"}
