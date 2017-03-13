#Wilfred Githuka
#Githka.com
#02 January 2016
#Exercise 15

#Import the argv module
from sys import argv

#Give argv the parameters
script, filename = argv

#Commans to open a file
txt = open(filename)

#Print out the filename
print "Here's your file %r:" % filename

#Print out the contents of the File, giving the Read method a blanc
print txt.read()

#Print out the File contents again
#print "Type the filename again:"

#file_again = raw_input("> ")

#txt_again = open(file_again)
#print txt_again.read()

