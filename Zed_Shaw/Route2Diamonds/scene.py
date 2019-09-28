#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were included for  
#saluting Zed Shaw.

from collections import defaultdict

class Scene(object):


	#In most of rooms players should pick things up. Withouth them
	#they won't be able to pass through rooms they will attend
	#along their journeys. When they picked their staff it will be
	#added to their Thingy basket that is represented with the below
	#dictionary. These things can be put down or can have different values
	#depending on my intentions and user actions..
	Thingy = defaultdict()

	def enter(self):
		print "Not yet implemented. Subclass it and implement enter() to define functionality."

	@classmethod
	def basket(cls):
		basket = []
		for k, v in cls.Thingy.items():
			if v == True:
				basket.append(k)

		return basket

class Reception(Scene):

	exits = {'left': 'scorpion', 'middle': 'knife', 'right': 'meat'}

	def __init__(self):
		self.Thingy['Yellow_key'] = False


	def enter(self):

		print "\nYou are in a dark room!"

		if self.Thingy['Yellow_key'] == True:

			print "You can see three doors:"
			print "left, middle, right!"

		else:

			print "You can see three doors:"
			print "left, middle, right"
			print "and a yellow key on the floor!"

		while True:
#		print "What do you do next?"
			print ("You have the following items: %r" % Scene.basket())
			print  ("_"*10)
			next = raw_input('\nWhat do you do next? |-> ')

			if 'pick' in next  in next:
				print "Key picked, well done!"
				self.Thingy['Yellow_key'] = True

			elif self.exits.get(next):
				print (self.exits.get(next))
				return self.exits.get(next)

			elif 'drop' in next:
				print "Key dropped!"
				self.Thingy['Yellow_key'] = False
			else:
				print "I dont't uderstand!"
				print "Try something else pls!"


class MeatRoom(Scene):

	def __init__(self):
		 self.Thingy['Big_meat_chunk'] = False

	def enter(self):

		print "\nYou enter a room through a dodgy bridge."
		print "There is a huge piece of meat on a chopping block!"

		while True:

			print ("You have the following items: %r" % Scene.basket())
			print  ("_"*10)
			next = raw_input("\nWhat do you do next? |-> ")

			if 'pick' in next and self.Thingy['Big_meat_chunk'] == False:
				print "Well done! You have a massive chunk of meat!"
				self.Thingy['Big_meat_chunk'] = True

			elif 'drop' in next:
				print "Meat dropped!"
				self.Thingy['Big_meat_chunk'] = False

			elif 'bridge' in next or 'leave' in next and self.Thingy['Big_meat_chunk'] == False:
				return 'reception'

class KnifeRoom(Scene):

	def enter(self):
		print "You're in KnifeRoom!"
		return 'dead'

class Scorpions(Scene):

	def enter(self):
		pass

class DiamondRoom(Scene):

	def enter(self):
		pass

class GoldRoom(Scene):

	def enter(self):
		pass

class KoiPondRoom(Scene):

	def enter(self):
		pass


class Escape(Scene):

	def enter(self):
		pass

class Dead(Scene):
	quips =['My dog is better at this!']
	def enter(self):
		print "You're dead!"
		exit(1)


