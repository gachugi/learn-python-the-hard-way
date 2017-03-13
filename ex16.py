#Wilfred Githuka
#Githuka.com
#Exercise16

from sys import argv

script, filename = argv

print "Reading the contents of %r." % filename

contents = open(filename)
print contents.read() 

print "Now, we are going to erase the contents of %r." % filename
print "If you do not want that, hit CTRL-C (`C)."
print "If you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to write there to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#target.write(line1\nline2\nline3)

print "And finally, we close it."
target.close()

