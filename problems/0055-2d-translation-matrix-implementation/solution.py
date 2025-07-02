import numpy as np
def translate_object(points, tx, ty):
  translated_points = points
  for point in translated_points:
    point[0] += tx
    point[1] += ty
    
  return translated_points