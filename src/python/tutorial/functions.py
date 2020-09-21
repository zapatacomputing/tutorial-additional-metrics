from sklearn.metrics import f1_score

def calculate_f1_score(predictions, labels):
    f1 = f1_score(predictions, labels)
    return f1
