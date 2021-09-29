# K06 StI/O: Divine your Destiny!
## Team Elon Musk: Aryaman Goenka, Haotian Gan, Tomas Acuna 

### File (CSV) I/0. 
* We inputed the csv file using csv on python. To transfer the data into a dictionary, we made each occupation represent a key with its weight being its respective value pair. 

### Dictionary: What is it good for?
* A dictionary was useful becuase it allowed for one value to be specifically assigned to another. It also did not allow duplciate keys, meaning that there was only one reference for each occupation.

### List:
* In order for a list to work in this situation, you would need to use a nested list, but it made more sense to use a dictionary. 

### Github Markdown
* (#) Represents the Largest Heading, and as you add more # the headings become smaller
* Adding * at the start of a line creates a bullet point

### Weighted Randomized Selection
* The weighted randomized selection works by generating a random float from 0-100 and subtracting the percent chance of each occupation from this float until it reaches 0, at which point the name of the last subtracted occupation is printed.