import os
from flask import Blueprint, request, jsonify
from services.forward_service import forward_data
from models.shipment_schema import validate_shipment
from utils.regex_utils import extract_shipment_data

shipment_bp = Blueprint('shipment', __name__)
@shipment_bp.route('/update', methods=['POST'])

def update_shipment():
  
  data = request.get_json()
  if "message" not in data:
    return jsonify({"error": "Message field is required"}), 400
  
  message = data["message"]
  
  extracted = extract_shipment_data(message)
  is_valid, msg = validate_shipment(extracted)
  
  if not is_valid:
    return jsonify({"error": msg}), 400
  
  payload = {
        **extracted,
        "raw_message": message
    }

  forward_data(payload)

  return jsonify({
        "status": "success",
        **extracted
    })
  
