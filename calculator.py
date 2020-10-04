bake = True
i = 0
while bake:
    inpt = input("Enter the numbers with operation :\n")

    if '+' in inpt:
        o = inpt.split('+')
        print(o)
        for value in o:
            try:
                int(value)
                done1 = True
            except:
                print("Please Enter integer value.")
                bake = False
            if done1:
                li = list()
                li.append(value)
                i = i+1
        print(li)
    if i == 2:
        bake = False