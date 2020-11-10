from prettytable import PrettyTable
from PackageHimaloy import my_dictionary, createfile

x = PrettyTable()
dic = my_dictionary()
x.field_names = ["Name", "Money"]
rate = int(input("Enter rate per hour: "))
path = "../Files/wages.txt"
file = open(path)
for line in file:
    lin = line.rstrip()
    slp = lin.split()
    name = slp[0]
    time = float(slp[1])
    if time <= 40:
        pay = time * rate
        dic.add(pay, name)
    else:
        t = time - 40
        py = 40 * rate
        p = t * (1.5 * rate)
        pay = p + py
        dic.add(pay, name)
for name, wage in dic.items():
    x.add_row([name, wage])
createfile("Wages", str(x))