import numpy as np

def ema_update(ema_params, model_params_list, decay):
    """
    Compute the Exponential Moving Average of model parameters over training steps.
    
    Args:
        ema_params: numpy array, initial EMA parameters
        model_params_list: list of numpy arrays, model params at each training step
        decay: float, EMA decay rate in [0, 1]
    Returns:
        Final EMA parameters as a (nested) list, rounded to 4 decimal places
    """
    # Your code here
    final_ema_params = ema_params
    for model_params in model_params_list:
        final_ema_params = decay * final_ema_params + (1 - decay) * model_params
        
    return np.round(final_ema_params,4).tolist()