import math

def softmax(scores: list[float]) -> list[float]:
	probabilities = []
	sum_exp = sum(math.exp(score) for score in scores)
	for score in scores:
		probabilities.append(round(math.exp(score) / sum_exp, 4))
	return probabilities