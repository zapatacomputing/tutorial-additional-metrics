from sklearn.metrics import f1_score
import json
from json import JSONEncoder
import numpy as np

def calculate_f1_score(predictions, labels):
    f1 = f1_score(predictions, labels)
    return f1

def save_json(result, filename) -> None:
    """
    Saves data as JSON.
    Args:
        result (ditc): of data to save.
        filenames (str): file name to save the data in
            (should have a '.json' extension).
    """
    try:
        with open(filename,'w') as f:
            result["schema"] = "orquestra-v1-data"
            f.write(json.dumps(result, indent=2, cls=NumpyArrayEncoder)) 

    except IOError:
        print(f'Error: Could not open {filename}')

def read_json(filename) -> dict:
    """
    Loads data from JSON.
    Args:
        filename (str): the file to load the data from.
    Returns:
        data (dict): data that was loaded from the file.
    """
    data = {}
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except IOError:
            print(f'Error: Could not open {filename}')

    return data

def calculate_f1_score_step(labels, predictions):
    lab = read_json(labels)['labels']
    pred = read_json(predictions)['predictions']

    f1_score = [calculate_f1_score(pred, lab)]

    f1_score_dict = {}
    f1_score_dict['f1_score'] = f1_score

    # SERIALIZE HERE
    save_json(f1_score_dict, 'f1_score.json')
