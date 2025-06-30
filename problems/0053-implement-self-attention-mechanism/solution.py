import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
  Q = X.dot(W_q)
  K = X.dot(W_k)
  V = X.dot(W_v)

  return Q,K,V

def self_attention(Q, K, V):
  attention_output = (Q @ (K.T))/np.sqrt(K.shape[1])
  attention_output = np.exp(attention_output) / np.sum(np.exp(attention_output), axis=1, keepdims=True)
  return attention_output @ V
