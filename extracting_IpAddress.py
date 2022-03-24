#importing modules
import os
import re

#opening and reading the file
def openFile(document):
    try:
        file = open(document, 'r')
        return file
    except:
        print("File not found")
        quit ()
        
document = ("Enter path to wordlist file here: ")
file = openFile(document)

#declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

#Initializing the list objects
lst = []

#Extracting the IP address
for line in file:
    lst.append(pattern.search(line)[0])


#writing the extracted IP addresses in a text file.
lst = open('result.txt', 'w')
lst.close()

#Checking if the IP address has been written in that file
lst = open('result.txt', 'r')
print (lst.read())
lst.close()