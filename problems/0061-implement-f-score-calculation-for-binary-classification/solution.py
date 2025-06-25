import numpy as np

def precision(y_true, y_pred):
	# Your code here
  true_positives = 0
  false_positives = 0
  for i in range(len(y_true)):
    true_positives += y_pred[i] == 1 and y_pred[i] == y_true[i]
    false_positives += y_pred[i] == 1 and y_pred[i] != y_true[i]

  return true_positives / (true_positives + false_positives)

def recall(y_true, y_pred):
    numerator, denominator = 0, 0
    for i in range(len(y_true)):
      numerator += y_pred[i] == 1 and y_pred[i] == y_true[i]
      denominator += y_pred[i] == 0 and y_pred[i] != y_true[i]

    return numerator / (numerator + denominator) if numerator + denominator > 0 else 0.0

def f_score(y_true, y_pred, beta):
  """
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
  precision_val, recall_va