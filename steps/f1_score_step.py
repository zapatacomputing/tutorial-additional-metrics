from additional-metrics.functions import calculate_f1_score
from additional-metrics.utils import read_json, save_json

def calculate_f1_score_step(labels, predictions):
    lab = read_json(labels)['labels']
    pred = read_json(predictions)['predictions']

    f1_score = [calculate_f1_score(pred, lab)]

    f1_score_dict = {}
    f1_score_dict['f1_score'] = f1_score
    save_json(f1_score_dict, 'f1_score.json')
