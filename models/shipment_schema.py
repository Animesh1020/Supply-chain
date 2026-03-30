def validate_shipment(data):
  if not data["order_id"]:
    return False, "Order ID is required"
  if not data["shipment_id"]:
    return False, "Shipment ID is required"
  if not data["delivery_date"]:
    return False, "Delivery date is required"
  
  return True, "Validation successful"