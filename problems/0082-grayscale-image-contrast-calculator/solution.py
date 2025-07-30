import numpy as np

def calculate_contrast(img) -> int:
  """
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	# Your code here
  min_pixel, max_pixel = img[0][0], img[0][0]
  for pixel in img:
    for num in range(len(pixel)):
      min_pixel = min(min_pixel, pixel[num])
      max_pixel = max(max_pixel, pixel[num])

  return max_pixel - min_pixel