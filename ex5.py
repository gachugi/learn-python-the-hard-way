#Wilfred Githuka
#Learning Python
#Morning of Thursday 29 Dec 2016

name = 'Wilfred G Githuka'
age = 29 #Not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height * 2.54
weight_kg = weight * 0.454

print "Lets talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d kgs heavy."% weight_kg
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %r, %r, and %d I get %d."% (age, height_cm, 
weight_kg, age +  height_cm + weight_kg)
