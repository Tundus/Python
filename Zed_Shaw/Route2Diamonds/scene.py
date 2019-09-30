#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were included for  
#saluting Zed Shaw.

from collections import defaultdict
from random import randint
from db_connect import *

class Scene(object):


	#In most of rooms players should pick things up. Withouth them
	#they won't be able to pass through rooms they will attend
	#along their journeys. When they picked their staff it will be
	#added to their Thingy basket that is represented with the below
	#dictionary. These things can be put down or can have different values
	#depending on my intentions and user actions..
	Thingy = dict()

	def __init_(self):
		pass

	def enter(self):
		print "Not yet implemented. Subclass it and implement enter() to define functionality."

	@classmethod
	def basket(cls):
		basket = []
		for k,v in cls.Thingy.items():
			if v == True:
				split_key = k.split('_')
				readable_key = ' '.join(split_key)
				basket.append(readable_key)
		return basket

class Kickoff(Scene):

	def __init__(self):
		r_tools, room, health = load_data('Player1')
	
		for k,v in decode_dict(r_tools).items():
			self.Thingy[k] = v

#		print ("These are the things in recovered dict: %r" % self.Thingy)


class Reception(Scene):

	exits = {'left': 'scorpion', 'middle': 'knife', 'right': 'meat'}

	def __init__(self):
		if not self.Thingy.has_key('Yellow_key'):
			self.Thingy['Yellow_key'] = False

	def enter(self):

		print "\nYou are in a dark room!"

		if self.Thingy['Yellow_key'] == False:

			print "A yellow key lays on the floor!"

		while True:
			print "\n*You have the following door options: %r" % self.exits.keys()
			print ("#You have the following items: %r" % Scene.basket())
			next = raw_input('\nWhat do you do next? |-> ')
			print  ("_"*10)

			if 'pick' in next  in next:
				print "Key picked, well done!"
				self.Thingy['Yellow_key'] = True

			elif self.exits.has_key(next):
				return self.exits.get(next)

			elif 'drop' in next and 'key' in next:
				print "Key dropped!"
				self.Thingy['Yellow_key'] = False

			else:
				print "I dont't uderstand!"
				print "Try something else pls!"


class MeatRoom(Scene):

	exits = {'bridge': 'reception'}

	def __init__(self):
		if not self.Thingy.has_key('Big_meat_chunk'):
			self.Thingy['Big_meat_chunk'] = False

	def enter(self):

		print "\nYou enter a room through a dodgy bridge."
		print "There is a huge piece of meat on a chopping block!"

		while True:
			print "\n*You have the following door options: %r" % str(self.exits.keys())
			print ("#You have the following items: %r" % Scene.basket())
			next = raw_input("\nWhat do you do next? |-> ")
			print  ("_"*10)


			if 'pick' in next and self.Thingy['Big_meat_chunk'] == False:
				print "Well done! You have a massive chunk of meat!"
				self.Thingy['Big_meat_chunk'] = True

			elif 'drop' in next and 'meat' in next:
				print "Meat dropped!"
				self.Thingy['Big_meat_chunk'] = False

			elif (self.exits.has_key(next)) and self.Thingy['Big_meat_chunk'] == False:
				return 'reception'

			elif (self.exits.has_key(next)) and self.Thingy['Big_meat_chunk'] == True:
				print ("This is a dodgy bridge and you're too heavy with the meat.")
				print ("It collapses and you fall into a chasm!")
				return 'dead'

			elif ('cut' in next or 'slice' in next) and self.Thingy['Big_kitchen_knife'] == True and self.Thingy['Big_meat_chunk'] == False:
				print "Well done! You have a slice of meat!"
				self.Thingy['Meat_slice'] = True


			elif ('cut' in next or 'slice' in next) and self.Thingy['Big_kitchen_knife'] == True and self.Thingy['Big_meat_chunk'] == True:
				print "Nothing is here to cut or slice!"

			elif self.exits.has_key(next):
				self.exits.get(next)

class KnifeRoom(Scene):

	exits = {'right': 'reception'}

	def __init__(self):
		if not self.Thingy.has_key('Big_kitchen_knife'):
			self.Thingy['Big_kitchen_knife'] = False

	def enter(self):

		print "You step in a cold room."

		if self.Thingy['Big_kitchen_knife'] == False:

			print "On the floor you can see a big kitchen knife!"
			print "It was frozen in an ice cube 5000 years ago!"
		else:

			print "A big wet spot in the middle but nothing else!"
			print "Melted ice maybe?"


		while True:
			print "\n*Your door options are: %r" % self.exits.keys()
			print ("#You have the following items: %r" % Scene.basket())
			next = raw_input("\nWhat do you do next? |-> ")
			print  ("_"*10)

			if 'pick' in next and self.Thingy['Big_kitchen_knife'] == False:
				print "Who said it is cold enough down here for the ice?"
				print "It has long melted! Good spot mate!"
				self.Thingy['Big_kitchen_knife'] = True

			elif 'drop' in next and 'knife' in next:
				print "Knife dropped!"
				self.Thingy['Big_kitchen_knife'] = False

			elif self.Thingy['Big_kitchen_knife'] == False and ('smash' in next or 'fire' in next or 'melt' in next):
				print "You can't do that! You don't have the right equipment!"
				print "Try something else!"

			elif self.exits.has_key(next):
				return self.exits.get(next)

			else:
				print "Sorry, I dont' understand!"

class Scorpions(Scene):

	exits = {'left': 'scorpion', 'middle': 'knife', 'right': 'meat'}

	def __init__(self):
		if not self.Thingy.has_key('Yellow_key'):
			self.Thingy['Yellow_key'] = False

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
	quips =['My dog is better at this!',
		'You kinda suck at this!',
		'Your mum would be proud...if you were smarter!',
		'Such a looser!'
]
	def enter(self):
		print Dead.quips[randint(0, len(self.quips)-1)]
		print "You're dead!"
		exit(1)


