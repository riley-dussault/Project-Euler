#This is a program with all of the Project Euler problems that I completed. 
#I wanted to make all of the problems executable through one program because it added a level of challenge and made it much easier to see the work I have done.
from time import sleep
import sys
import fractions

def main():
	selections = {
		"1" : problem1,
		"2" : problem2,
		"3" : problem3,
		"4" : problem4,
		"5" : problem5,
		"6" : problem6,
		"0" : False,
	}

	printheader()
	while True:
		selection = userselection()
		if selections[selection]:
			print ("Running")
			selections[selection] ()
		else:
			print ("        ")
			print ("Breaking")
			break

def printheader():
	phrases = ["Project Euler"]

	for phrase in phrases:          
	    for c in phrase:          
	        print(c, end='')    
	        sys.stdout.flush()  
	        sleep(0.1)          
	    print('')               

def userselection():
	return input("Enter a number between 1 and 6 for Answer: ")

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
    	return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def problem1():
	result = 0
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			result += i

	print (result)

def problem2():
	result = 0
	i = 1
	while fibonacci(i) <= 4000000:
		if fibonacci(i) % 2 == 0:
			result += fibonacci(i)
		i += 1
	print(result)

def problem3():
	n = 600851475143
	i = 2

	while i * i < n:
	    while n%i == 0:
	        n = n / i
	    i = i + 1
	print(n)

def problem4():
	product = max(a * b
		for a in range(100, 1000)
		for b in range(100, 1000)
		if str(a * b) == str(a * b)[ : : -1])
	print (str(product))

def problem5():
	answer = 1
	for i in range(1,21):
		answer *= i // fractions.gcd(i, answer)
	print (str(answer))

def problem6():
	N = 100
	s = sum(i for i in range(1, N + 1))
	s2 = sum(i**2 for i in range(1, N + 1))
	print (str(s**2 - s2))

main()