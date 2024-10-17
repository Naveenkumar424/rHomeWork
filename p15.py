#Factorial of a number
def fact(n):
    if(n == 0):
        return 1
    return n*fact(n-1)
#end of fact
#main section
n = int(input("Enter n:"))
print(f"Fact({n}):{fact(n)}")
#End of code
