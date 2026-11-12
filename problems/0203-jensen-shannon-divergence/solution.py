import numpy as np

def jensen_shannon_divergence(P: list[float], Q: list[float]) -> float:
    """
    Compute the Jensen-Shannon Divergence between two probability distributions.
    
    Args:
        P: First probability distribution
        Q: Second probability distribution
    
    Returns:
        Jensen-Shannon Divergence value
    """
    # Your code here
    p = np.array(P)
    q = np.array(Q)
    m = (p + q)/2
    d_KL_pm = np.sum(np.where(p > 0, p*np.log(p/m), 1e-10), axis = 0)
    d_KL_qm = np.sum(np.where(q > 0, q*np.log(q/m), 1e-10), axis = 0)
    jsd_pq = 1/2 * (d_KL_pm + d_KL_qm)
    return jsd_pq