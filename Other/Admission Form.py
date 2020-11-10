import time


class Student:
    def __init__(self, name, rank, percentage, age):
        self.name = name
        self.rank = rank
        self.percentage = percentage
        self.age = age

    def check(self):
        if self.rank <= 5000:
            rankcheck = True
        else:
            rankcheck = False
        if self.percentage > 95:
            percentagecheck = True
        else:
            percentagecheck = False
        if self.age >= 18 and self.age <= 25:
            agecheck = True
        else:
            agecheck = False
        if agecheck and percentagecheck and rankcheck:
            print('Please wait.....')
            time.sleep(3)
            print("Proccessing.....")
            time.sleep(5)
            return print(f"{self.name} you are selected!!!👏👏👏👏🎉🎉🎉🎉✌✌")
        else:
            print('Please wait.....')
            time.sleep(3)
            print("Proccessing.....")
            time.sleep(5)
            return print("Better Luck next time")


# While loop starts here
while True:
    name = input("Enter Your name:")
    if name != '':
        break
    else:
        print("\nName can not be blank\n")
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

while True:
    rank = input("Enter your boards rank:")
    if rank != '':
        try:
            rank = int(rank)
            break
        except:
            pass
    else:
        print("\nRank can not be blank\n")
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

while True:
    per = input("Enter your boards percentage:")
    if per != '':
        try:
            per = per.replace('%', '')
            per = float(per)
            break
        except:
            pass
    else:
        print("\nPercentage can not be blank\n")
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

while True:
    age = input("Enter your age:")
    if age != '':
        try:
            age = int(age)
            break
        except:
            pass
    else:
        print("\nAge can not be blank\n")


# While loop ends here
def nameformating(name):
    index1 = name[0]
    new = index1.upper()
    inde2 = name[1:]
    newt = inde2.lower()
    name = new + newt
    return name


name = nameformating(name)
Student_info = Student(name, rank, per, age).check()
