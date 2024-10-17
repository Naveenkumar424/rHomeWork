#Fibonacci series
n = int(input("Enter n:"))
f0 = 0
f1 = 1
while(f1 <= n):
    print(f1)
    f2 = f0+f1
    f0 = f1
    f1 = f2
#end of code