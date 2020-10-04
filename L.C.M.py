num1 = input("Enter Num 1:\t")
num2 = input("Enter Num 2:\t")
try:
    num1 = int(num1)
    num2 = int(num2)
except Exception as e:
    print(e)
maxnum = max(num1, num2)
while True:
    if maxnum % num1 == 0 and maxnum % num2 == 0:
        break
    maxnum = maxnum + 1
print(f"L.C.M of {num1} and {num2} is {maxnum}")