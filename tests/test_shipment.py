from utils.regex_utils import extract_shipment_data

class TestShipmentDataExtraction:
  def test_extract_valid_message(self):
    message = "Order ORD12345 with Shipment SHP56789 will arrive on 2026-03-30."
    result = extract_shipment_data(message)
    
    assert result["order_id"] == "ORD12345"
    assert result["shipment_id"] == "SHP56789"
    assert result["delivery_date"] == "2026-03-30"
  
  def test_extract_message_missing_data(self):
    message = "Order ORD12345 will arrive on 2026-03-30."
    result = extract_shipment_data(message)
    
    assert result["order_id"] == "ORD12345"
    assert result["shipment_id"] is None
    assert result["delivery_date"] == "2026-03-30"
  
  def test_extract_message_missing_date(self):
    message = "Order ORD12345 with Shipment SHP56789 will arrive soon."
    result = extract_shipment_data(message)
    
    assert result["order_id"] == "ORD12345"
    assert result["shipment_id"] == "SHP56789"
    assert result["delivery_date"] is None
    
  def test_extract_message_all_data_missing(self):
    message = "No shipment information available."
    result = extract_shipment_data(message)
    
    assert result["order_id"] is None
    assert result["shipment_id"] is None
    assert result["delivery_date"] is None