import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
  num_batches = X.shape[0] // batch_size + 1 if X.shape[0] % batch_size else X.shape[0] // batch_size
  not_fit = X.shape[0] % batch_size
  batches = []
  for idx in range(num_batches):
    new_batch_x = []
    new_batch_y = [] if y is not None else None

    if not_fit and idx == num_batches - 1:
      new_batch_x.append(X[idx * batch_size:])
      if y is not None:
        new_batch_y.append(y[idx * batch_size:])
    else:
      new_batch_x.append(X[idx * batch_size : idx * batch_size + batch_size])
      if y is not None:
        new_batch_y.append(y[idx * batch_size : idx * batch_size + batch_size])

    batches.append((new_batch_x, new_batch_y) if y is not None else (new_batch_x))

  return batches