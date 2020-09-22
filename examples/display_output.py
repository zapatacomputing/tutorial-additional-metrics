import json
import pandas as pd

import json

# Insert file path in the next line
with open('./examples/additional-metrics-output.json') as f:
    data = json.load(f)

steps = list(data.keys())

for step in steps:
    if 'predictions' in data[step]:
        print("Predictions")
        for p in data[step]['predictions']['predictions']:
            print(p['predictions'])
    if 'f1_score' in data[step]:
        print("F1-score:")
        print(data[step]['f1_score']['f1_score'][0]['f1_score'])
