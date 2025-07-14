import numpy as np 
from scipy import stats

def descriptive_statistics(data):
	# Your code here
  data = np.array(data)
  stats_dict = {
        "mean": np.mean(data),
        "median": np.median(data),
        "mode": stats.mode(data).mode,
        "variance": np.round(np.var(data),4),
        "standard_deviation": np.round(np.std(data),4),
        "25th_percentile": np.percentile(data, 25),
        "50th_percentile": np.percentile(data, 50),
        "75th_percentile": np.percentile(data, 75),
        "interquartile_range": np.percentile(data, 75) - np.percentile(data, 25)
  }
  
  return stats_dict