import re

def extract_shipment_data(message):
  order_pattern = re.compile(r"ORD\d+")
  shipment_pattern = re.compile(r"SHP\d+")
  date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")

  order_id = order_pattern.search(message)
  shipment_id = shipment_pattern.search(message)
  delivery_date = date_pattern.search(message)

  return {
    "order_id": order_id.group() if order_id else None,
    "shipment_id": shipment_id.group() if shipment_id else None,
    "delivery_date": delivery_date.group() if delivery_date else None
  }