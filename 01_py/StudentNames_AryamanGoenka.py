##
# Aryaman Goenka    
# Soft Dev
# 2021/09/23
##

import random

def read():
    lines = []
    with open('studentnames.txt') as f:
        lines = f.readlines()
    return lines

def divideClass():
    pd1 = []
    pd2 = []
    lines = read()

    for i in lines:
        randomnum = random.randint(0,2)
        if "PD1" in i:
            num = i.index(" PD1")
            i = i.replace(" PD1", "", num)
            pd1.append(i)
        else:
            pd2.append(i)
    return pd1, pd2

def generateRandomStudent():
    pd1, pd2 = divideClass()

    lenpd1 = len(pd1)
    lenpd2 = len(pd2)
    randompd = random.randint(1,3)

    if randompd <= 1:
        randomstudent = random.randint(0, lenpd1) - 1
        return (pd1[randomstudent])

    elif randompd >1 :
        randomstudent = random.randint(0, lenpd2) - 1
        return (pd2[randomstudent])

def main():
    print(generateRandomStudent())
        
if __name__ == "__main__":
    main()