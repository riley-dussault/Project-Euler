def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
i = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(i):
    print (fibonacci(i)),