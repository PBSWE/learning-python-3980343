# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
# sample = open('textfile.txt', 'w+')
# sample.write('Sample text to our file.')
# sample.close()

# Open the file for appending text to the end
sample = open('textfile.txt', 'a+')
sample.write('More sample text appended to our existing file.')
sample.close()

# write some lines of data to the file


# close the file when done