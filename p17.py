#factorial of fibonnaci series
def fact(n):
    if(n == 0):
        return 1
    return n*fact(n-1)
#end of fact
#main
n = int(input("Enter n:"))
f0 = 0
f1 = 1
while(f1 <= n):
    print(fact(f1))
    f2 = f0 + f1
    f0 = f1
    f1 = f2
#end of code