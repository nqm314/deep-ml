import numpy as np

def gcn_layer(A: np.ndarray, X: np.ndarray, W: np.ndarray) -> np.ndarray:
    """
    Perform a single GCN layer forward pass.
    
    Args:
        A: Adjacency matrix of shape (N, N)
        X: Node feature matrix of shape (N, F_in)
        W: Weight matrix of shape (F_in, F_out)
        
    Returns:
        Output feature matrix of shape (N, F_out)
    """
    A_self_loops = A + np.eye(A.shape[0], A.shape[0])
    # print(A_self_loops)
    d_inv_sqrt = np.diag(np.sum(A_self_loops, axis=1)**(-1/2))
    # print(d_inv_sqrt)
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0
    # print(d_inv_sqrt)
    A_norm = d_inv_sqrt @ A_self_loops @ d_inv_sqrt
    # print(A_norm)
    output = A_norm @ X @ W
    output = np.maximum(0, output)
    return output