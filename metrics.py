from routes.shipments import shipments_db

def calculate_metrics():
    total_shipments = len(shipments_db)
    delivered = sum(1 for s in shipments_db if s.status == "Delivered")
    return {
        "total_shipments": total_shipments,
        "delivered": delivered,
        "pending": total_shipments - delivered
    }
