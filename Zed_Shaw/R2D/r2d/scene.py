#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were included for  
#saluting Zed Shaw.

from collections import defaultdict
from random import randint
from db_connect import *
from lexicon import *
from parser import *

class Scene(object):


	#In most of rooms players should pick things up. Withouth them
	#they won't be able to pass through rooms they will attend
	#along their journeys. When they picked their stuff it will be
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

	@classmethod
	def set_comp(cls, ans_s={}, exit_s={}):
		w_set = ans_s.intersection(exit_s) 
		if len(w_set) == 1:
			return list(w_set)
		else:
			return None

	@classmethod
	def natural_lang(cls, user_input):
		try :
			word_list = scan(user_input)
			pwl = parse_sentence(word_list)
			parsed_input = [pwl.subject, pwl.verb, pwl.object, pwl.number]

			if not pwl.number:
				parsed_input.pop(-1)
			
			parsed_sentence = ' '.join(parsed_input)
			return parsed_sentence

		except ParserError as err:
			return ('ParserError', err)


class Load_tools(Scene):

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
			parsed_sentence = Scene.natural_lang(next)
			has_direction = parsed_sentence.split()[-1]

			if parsed_sentence == "player pick key":
				if  self.Thingy['Yellow_key'] == False:
					print "Key picked, well done!"
					self.Thingy['Yellow_key'] = True
				else:
					print "What key please? You already have a key!"

			elif  peek(scan(has_direction)) == 'direction':
				return self.exits.get(has_direction)

			elif parsed_sentence == 'player drop key':
				if self.Thingy['Yellow_key'] == True:
					print "Key dropped!"
					self.Thingy['Yellow_key'] = False
				else:
					print "Sorry you don't have a key to drop!"

			elif parsed_sentence[0] == 'ParserError':
				print parsed_sentence[1]

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
			parsed_sentence = Scene.natural_lang(next)
			has_direction = parsed_sentence.split()[-1]


			if parsed_sentence == 'player pick meat':
				if self.Thingy['Big_meat_chunk'] == False:
					print "Well done! You have a massive chunk of meat!"
					self.Thingy['Big_meat_chunk'] = True
				else:
					print 'Don\'t be greedy'

			elif parsed_sentence == 'player drop meat':
				if self.Thingy['Big_meat_chunk'] == True:
					print "Meat dropped!"
					self.Thingy['Big_meat_chunk'] = False
				else:
					print "You don't have anything to drop!"

			elif peek(scan(has_direction)) == 'direction':
				if self.Thingy['Big_meat_chunk'] == True:
					print ("This is a dodgy bridge and you're too heavy with the meat.")
					print ("It collapses and you fall into a chasm!")
					return 'dead'

				elif self.Thingy['Big_meat_chunk'] == False:
					return self.exits.get(has_direction)

			elif parsed_sentence == 'player cut meat' or parsed_sentence == 'player slice meat':
				if  self.Thingy['Big_kitchen_knife'] == True:
					if self.Thingy['Big_meat_chunk'] == True:
						print "Congrats! You cut the meat in half you already had!"

					elif self.Thingy['Big_meat_chunk'] == False: 
						print "Well done! You have a slice of meat!"

					self.Thingy['Meat_slice'] = True

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
			parsed_sentence = Scene.natural_lang(next)
			has_direction = parsed_sentence.split()[-1]

			if parsed_direction == 'player pick knife':
				if self.Thingy['Big_kitchen_knife'] == False:
					print "Who said it is cold enough down here for the ice?"
					print "The ice has long melted! Good spot mate!"
					self.Thingy['Big_kitchen_knife'] = True
				elif self.Thingy['Big_kitchen_knife'] == True:
					print "What do you mean by that? There is no knife is here!"

			elif parsed_sentence == 'player drop knife':
				if self.Thingy['Big_kitchen_knife'] == True:
					print "Knife dropped!"
					self.Thingy['Big_kitchen_knife'] = False
				elif self.Thingy['Big_kitchen_knife'] == False:
					print "Pardon?"

			elif parsed_sentence == 'player smash ice' or parsed_sentence == 'player burn ice':
				if self.Thingy['Big_kitchen_knife'] == False:
					print "You can't do that! You don't have the right equipment!"
					print "Try something else!"

			elif peek(scan(has_direction) == 'direction':
				return self.exits.get(has_direction)

			else:
				print "Sorry, I dont' understand!"

class Scorpions(Scene):

	exits = {'left': 'scorpion', 'middle': 'knife', 'right': 'meat'}

	def __init__(self):
		pass

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


#__all__ = [Load_tools, Scene]
