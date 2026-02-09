#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#
    
# Open the file and read the contents
sample = open("textfile.txt", "r")
if sample.mode == "r":
    # use the read() function to read the entire file
    # contents = sample.read()
    # print(contents)
    lines = sample.readlines()
    for line in lines:
        print(line)
