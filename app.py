from flask import Flask
from routes.shipment_routes import shipment_bp

app = Flask(__name__)
app.register_blueprint(shipment_bp)

@app.route('/')

def home():
  return {"status": "ok", "services": "supply_chain_shipment"}

if __name__ == "__main__":
  app.run(debug = True)