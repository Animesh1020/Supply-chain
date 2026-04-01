from flask import Blueprint, request, jsonify
from utils.regex_utils import extract_data
from models.shipment_schema import validate_data
from services.forward_service import forward_data

shipment_bp = Blueprint("shipment", __name__)

@shipment_bp.route("/update", methods=["POST"])
def update_shipment():
    data = request.get_json()

    if "message" not in data:
        return jsonify({"error": "message required"}), 400

    message = data["message"]

    extracted = extract_data(message)

    valid, msg = validate_data(extracted)

    if not valid:
        return jsonify({"error": msg}), 400

    extracted["raw_message"] = message

    forward_data(extracted)

    return jsonify({
        "status": "success",
        "order_id": extracted["order_id"],
        "shipment_id": extracted["shipment_id"],
        "delivery_date": extracted["delivery_date"]
    })