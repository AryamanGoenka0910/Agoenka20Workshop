##
# Elon Musk: Haotian Gan, Aryaman Goenka, Tomas Acuna (Interm Member While Sean is Out)  
# Soft Dev
#
# K06 StI/O: Divine your Destiny!/Python Refresher/Write a Python script to read the file and build an appropriate dictionary from it.
# Create a function that returns a randomly selected occupation where the results are weighted by the percentage given.
#
# 2021/09/28
#
#
##

# SUMMARY OF TRIO DISCUSSION
# We First Discussed as a group the best way to tackle this problem 
# We then divided the work and began solving the problem to the best of our abilites

# DISCOVERIES
# It is a good thing to note that you should never mutate the data unless it is extremely necessary. 

import csv, random

#Function to read csv file and transfer it to an approriate dictionary
def readfile():
    file = open("occupations.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    occupations = {}
    for row in csvreader:
        if header[1] != row[1]:
            occupations[row[0]] = row[1]
    file.close()
    return occupations

#Using the weights provided in percentages, generate a randomly selected occupation
def genorateRandom():
    occupations = readfile()
    ran = random.randint(1, 100)
    for row in occupations:
        holder = occupations.get(row)
        ran -= float(holder)
        if ran <= 0:
            return row
    return

#Run functions and print an output
def main():
    print(genorateRandom())

if __name__ == "__main__":
    main()