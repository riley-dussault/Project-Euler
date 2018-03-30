def problem4():
	product = max(a * b
		for a in range(100, 1000)
		for b in range(100, 1000)
		if str(a * b) == str(a * b)[ : : -1])
	return str(product)


if __name__ == "__main__":
	print(problem4())