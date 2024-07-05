import json

class JsonHandler:
    def read_json(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data

    def write_json(self, data, file_path):
        with open(file_path, 'w') as f:
            json.dump(data, f)

    def check_key(self, data, key):
        return key in data