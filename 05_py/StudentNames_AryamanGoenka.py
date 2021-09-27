##
# Aryaman Goenka    
# Soft Dev
#
# K05: Better Living Through Amalgamation/Refresehing on Python/Refactoring code to generate random name from the 2 periods of softdev
#
# 2021/09/27
#
##

# SUMMARY OF TRIO DISCUSSION
# We discussed how my code works and talked about parameterizing the code. 
# We then went over our plans for refactoring our code to organize the names into 
# dictionaties using keys to separate the folks from period 1 and period 2. 

# DISCOVERIES
# Dictionaries are more useful than lists when working with two-dimensional data 
# (ie names from two class periods)

# QUESTIONS
# Should we parameterize our functions to take the output of other functions 
# instead of calling them inside other functions?


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
        
    softdev = {
        'pd1': pd1,
        'pd2': pd2
    }

    return softdev

def generateRandomStudent():
    softdev = divideClass()
    lenpd1 = len(softdev['pd1'])
    lenpd2 = len(softdev['pd2'])
    randompd = random.randint(1,3)

    if randompd <= 1:
        randomstudent = random.randint(0, lenpd1) - 1
        return (softdev['pd1'][randomstudent])
        

    elif randompd >1 :
        randomstudent = random.randint(0, lenpd2) - 1
        return (softdev['pd2'][randomstudent])

def main():
    print(generateRandomStudent())
        
if __name__ == "__main__":
    main()