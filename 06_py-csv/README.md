# K06 StI/O: Divine your Destiny!

## Team Elon Musk: Aryaman Goenka, Haotian Gan, Tomas Acuna

### File (CSV) I/0.

- To process the csv file, we first opened it with open(), then passed that into the csv module's csv.reader(). That gave us an iterable object, in which every iterable was a list of strings. The first element of each list is the first comma seperated value in the line -- in this project's case it was the occupation category (i.e. "Healthcare support"). The second element of each list is the second comma seperated value in the line -- in this project's case it was the percentage (i.e 9.8%). We iterated through each line of the object we got from csv.reader with:
```
for row in csvreader:
```

And added each occupation and it's respective percentage to a dictionary:
```
occupations[row[0]] = row[1]
```

### Dictionary: What is it good for?

- A dictionary was useful becuase it allowed for one value to be specifically assigned to another. It also did not allow duplciate keys, meaning that there was only one reference for each occupation. You use a dictionary by first creating a dictionary object using curly braces
```
myDict = {}
```
Then by adding elements with 
```
myDict["Your key here"] = "Your value here"
```
And accessing elements with
```
myDict["Your key here"]
```

Dictionaries come with a variety of useful methods, such as keys() or values() or get(). You can get the length of a dictionary with len() or by calling it's len method.
### List:

- Lists in python are zero-indexed and can grow as your add more elements. They can be iterated through using a for loop. In our assignment, each line in our csv was represented by the csv.reader() object as a list of strings. We iterated through this list of strings for each line, and added the strings to our dictionary.

### Github Markdown

- (#) Represents the Largest Heading, and as you add more # the headings become smaller
- Adding \* at the start of a line creates a bullet point
- Adding three backticks followed by text followed by three more backticks, makes your text formatted as code. 

### Weighted Randomized Selection

- In our assignment, we implemented a weighted randomized selection algorithm. We generated a random float between 0 and 100 (excluding 100) and iterated through our dictionary of occupations, subtracting the percentage chance of each occupation from this float until our float was less than or equal to zero, at which point we printed the name of the last subtracted operation. 