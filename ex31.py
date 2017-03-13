#Wilfred Githuka
#Learning Python Ex31.py
#20th February 2017
#Githuka.com

print "You enter a dark room with 2 doors, Do you go through Door 1 or Door 2?"

door = raw_input("> ")

if door == '1':
	print "There is a giant bear here eating a cheese cake, hat do u wanna do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off."
	elif bear == "2":
		print "The bear eats your legs off."
	else:
		print "Well, doing %s is probably better, bear runs away." % bear
	
 
elif door == "2":
	print "You stare into the endless abyss at Wilfred's retina."
	print "1. Blueberrie."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello."
	else:
		print "The insanity rots your eyes into a pool of muck."
	
else:
	print "You stumble around and fall on a knife and die."
