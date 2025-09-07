import json

def load_json_data(path):
    """Loads data from a JSON file.

    Args:
        path (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(path, 'r') as f:
        return json.load(f)