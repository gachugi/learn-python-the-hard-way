#Wilfred Githuka
#Githuka.io
#Learning Python Ex40

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_birthday = Song(["Happy birthday to you",
			"I dont want to get sued",
			"So I'll stop right here"])

bulls_on_parade = Song (["They arlly around the family",
			"With pockets full of shells"])

mary_had_a_little_lamb = Song(["Mary had a little lamb",
				"Which was as white as snow"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mary_had_a_little_lamb.sing_me_a_song()
