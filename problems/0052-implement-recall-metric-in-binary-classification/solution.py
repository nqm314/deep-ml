import numpy as np

def recall(y_true, y_pred):
    numerator, denominator = 0, 0
    for i in range(len(y_true)):
      numerator += y_pred[i] == 1 and y_pred[i] == y_true[i]
      denominator += y_pred[i] == 0 and y_pred[i] != y_true[i]
    
    return round(numerator / (numerator + denominator), 3) if numerator + denominator > 0 else 0.0