from flask import Blueprint, jsonify
from data_store import DataStore

data_bp = Blueprint('data', __name__)
data_store = DataStore()

@data_bp.route('/fetch-data', methods=['GET'])
def fetch_data():
    try:
        
        test_sample_data = [
            {"id": 1, "name": "Ironman", "description": "Stark Industries owner, Most powerful Avenger", "age": 50},
            {"id": 2, "name": "Batman", "description": "Person who wants to save Gotham city, comes out mostly at night", "age": 45},
            {"id": 3, "name": "Thor", "description": "God of Thunder, son of Odin", "age": 500},
        ]

        # Process and store data
        for item in test_sample_data:
            processed_item = data_store.process_data(item)
            data_store.store_processed_data(processed_item)

        return jsonify({
            "fetched_data": test_sample_data,
            "message": "Data fetched and processed successfully"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@data_bp.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    try:
        # Get processed data from memory
        processed_data = data_store.get_all_processed_data()
        return jsonify({"processed_data": processed_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
