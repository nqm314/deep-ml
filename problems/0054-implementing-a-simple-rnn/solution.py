import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
	# Your code here
  input_sequence = np.array(input_sequence)
  initial_hidden_state = np.array(initial_hidden_state)
  Wx = np.array(Wx)
  Wh = np.array(Wh)
  b = np.array(b)
  final_hidden_state = initial_hidden_state
  for i in range(len(input_sequence)):
    final_hidden_state = np.tanh(Wx.dot(input_sequence[i]) + Wh.dot(final_hidden_state) + b)
    # print(final_hidden_state)
  return final_hidden_state