import json
import pandas as pd

import json

# Insert file path in the next line
with open('./additional-metrics-output.json') as f:
    data = json.load(f)

steps = list(data.keys())

for step in steps:
    if 'predictions' in data[step].keys():
        print("Predictions:")
        for i in data[step]['predictions']['predictions']:
            print(i['predictions'])
        print()
    if 'f1_score' in data[step].keys():
        print("F1-Score:")
        print(data[step]['f1_score']['f1_score'])
