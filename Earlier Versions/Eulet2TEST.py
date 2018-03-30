def problem_2():
    s=0
    x=[1,1]
    while x[1] < 4000000:
        n=sum(x)
        if not n % 2: s+=n
        x=[x[1],n]
    return s