class DataStore:
    def __init__(self):
        self.storage = {}

    def process_data(self, data):
        try:
            processed_data = {
                "id": data["id"],
                "name": data["name"].upper(),
                "description": data["description"].upper(),
                "age": data["age"]
            }
            return processed_data
        except KeyError as e:
            raise ValueError(f"Missing key in data: {e}")
        except Exception as e:
            raise ValueError(f"Error processing data: {e}")

    def store_processed_data(self, data):
        self.storage[data['id']] = data

    def get_all_processed_data(self):
        return list(self.storage.values())
