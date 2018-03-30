def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
    	return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

result = 0
for i in range(1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		result += i

print (result)
