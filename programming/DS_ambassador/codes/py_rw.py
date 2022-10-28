"""
Read and write files in python
keywords: open, with, read, write, close
w: write, r: read, a: append
"""


# Open a file for writing and create it if it doesn't exist
f = open("textfile.txt", "w+")

# Open the file for appending text to the end
# f = open("textfile.txt", "a+")

# Write some lines of data to the file
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

f.close()  # Close the file when done



# Open the file back up and read the contents
f = open("textfile.txt", "r")
if f.mode == "r":
    # contents = f.read()
    fl = f.readlines() # a list
    for x in fl:
        print(x)
f.close()


# with statement (no need to close the file)
with open("textfile.txt", "r") as f:
    fl = f.readlines()
    for x in fl:
        print(x)
