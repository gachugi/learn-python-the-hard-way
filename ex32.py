#Wilfred Githuka
#Githuka.com
#Learning Python
#Ex 32.Py

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'appricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This frst kind of a for-loop goes through a list 

for number in the_count:
	print "Counting through... %d" % number

#same as above
for fruit in fruits:
	print "Fruits in list: %s" % fruit

#Also we can go through mixed lists too, we have to use %r when we dont know whats in it.

for i in change:
	print "I got %r" % i

#We can also build lists, first start with an empty one
elements = []

#Then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the lists." % i
	
	#Append is a function that lists understand 
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Elements was: %d" % i
