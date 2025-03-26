from pydantic import BaseModel
from typing import Literal

class Shipment(BaseModel):
    id: int
    tracking_number: str
    carrier: Literal["FedEx", "DHL"]
    destination: str
    status: Literal["In Transit", "Delivered", "Pending"]
