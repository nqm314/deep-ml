import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True, random_seed=None):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    if shuffle:
        if random_seed is not None:
            np.random.seed(random_seed)
            np.random.shuffle(X)
        else:
            np.random.shuffle(X)

    folds = np.array_split(X, k) 
    # print(folds) 

    train_test_indices = [] 
    for i in range(k):
        train_test_idx_i = []
        for j in range(k):
            if j == i:
                test_idx = folds[j]
                train_idx = np.concatenate(folds[:j] + folds[j+1:])
                train_test_idx_i.append((train_idx, test_idx))
        
        train_test_indices.append(train_test_idx_i)

    return train_test_indices