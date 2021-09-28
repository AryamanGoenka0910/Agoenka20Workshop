import csv, random

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


def genorateRandom():
    occupations = readfile()
    ran = random.randint(1, 100)
    for row in occupations:
        holder = occupations.get(row)
        ran -= float(holder)
        if ran <= 0:
            return row
    return


def main():
    print(genorateRandom())

if __name__ == "__main__":
    main()