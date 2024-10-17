#arithmatic operations on prime and fibonacci numbers from m to n
def prime(m,n):
    p = []
    for i in range(m,n+1):
        isp = True
        for j in range(2,i):
            if(i%j == 0):
                isp = False
        if(isp):
            p.append(i)
    return p
#end of prime
#fibonacci
def fib(m,n):
    f = []
    f0 = 0
    f1 = 1
    while(f1 <= n):
        if(f1 >= m):
            f.append(f1)
        f2 = f0+f1
        f0 = f1
        f1 = f2
    return f
#end of fibonnaci
#main section
m = int(input("Enter m:"))
n = int(input("Enter n:"))
p = prime(m,n)
f = fib(m,n)
print(f"Prime numbers from {m} to {n} are {p}")
print(f"Fibonacci numbers from {m} to {n} are {f}")
#end of code