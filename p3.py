#p1 for array of 5 elements
a = [1,1,6,4,2]
sum,diff,mul,div,mod = 0,0,1,1,1
for i in a:
    sum += i
    diff -= i
    mul *= i
    div /= i
    mod %= i
print(f"Sum:{sum}\nSub:{diff}\nMul:{mul}\nDiv:{div}\nMod:{mod}")
#end of code