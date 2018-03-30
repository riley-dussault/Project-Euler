import fractions

def problem5():
	answer = 1
	for i in range(1,21):
		answer *= i // fractions.gcd(i, answer)
	return str(answer)

print(problem5())