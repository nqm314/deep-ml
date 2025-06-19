import numpy as np
import math

def adaboost_fit(X, y, n_clf):
  n_samples, n_features = np.shape(X)
  w = np.full(n_samples, (1 / n_samples))
  clfs = []

  # Your code here
  for _ in range(n_clf):
    best_clf = {}
    min_error = float('inf')

    for feature_idx in range(n_features):
      X_feature = X[:, feature_idx]
      thresholds = np.unique(X_feature)
      polarity = 1
      for threshold in thresholds:
        predictions = np.ones(n_samples)
        predictions[polarity * X_feature < polarity * threshold] = -1
        missclassified = predictions != y
        error = np.sum(w[missclassified])

        if error > 0.5:
          error = 1 - error
          polarity = -polarity

        if error < min_error:
          min_error = error
          best_clf = {
              'polarity': polarity,
              'threshold': threshold,
              'feature_index': feature_idx,
              'predictions': predictions
          }

          p