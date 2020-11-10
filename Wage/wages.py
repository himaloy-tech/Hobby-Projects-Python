import pandas as pd
from PackageHimaloy import *

dict_obj = my_dictionary()
li = list()
li2 = list()
rate = int(input("Rate Per Hour:  "))

class Employee:
    def __init__(self, time, name, rate):
        self.name = name
        self.time = time
        if type(rate) == str:
            self.rate = int(rate)
        else:
            self.rate = rate

    def salary(self):
        if self.time <= 40:
            pay = self.time * self.rate
            dict_obj.add(pay, self.name)
        else:
            t = self.time - 40
            py = 40 * self.rate
            p = t * (1.5 * self.rate)
            pay = p + py
            dict_obj.add(pay, self.name)
        for k, v in dict_obj.items():
            self.name = k
            if self.name in li:
                continue
            else:
                li2.append(v)
                li.append(k)


def start(rate):
    file = open("../Files/wages.txt")
    for line in file:
        lin = line.rstrip()
        slp = lin.split()
        name = slp[0]
        time = float(slp[1])
        employee = Employee(time, name, rate).salary()
    d = {
        'Name': li,
        'Pay': li2
    }
    createfile('Payment', pd.DataFrame(d))


start(rate)
