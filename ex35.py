from sys import exit

def gold_room():
	print "This room is full of Gold, how much can you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man. learn how to type a number.")

	if how_much < 50:
		print "Nice, you're not gredy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fast bear is infront of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		next = raw_input("> ")
	
		if next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door,You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

def wilfred_room():
	print "Here you can see the great Wilfred."
	print "If he stares at you, you go insane."
	print "Do you flee or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		wilfred_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to ur left and right."
	print "Which one will u take?"

	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		wilfred_room()
	else:
		dead("Now you starve.")

start()

