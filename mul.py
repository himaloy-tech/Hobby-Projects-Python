num = int(input("Enter the Number: "))
result = [num*val for val in range(1, 11)]
i = 0
for index, item in enumerate(result):
    i += 1
    print(f"{num} x {index+1} = {item}")
class name():
    pass