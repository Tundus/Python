#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were included for  
#saluting Zed Shaw.

class Scene(object):


	#In most of rooms players should pick things up. Withouth them
	#they won't be able to pass through rooms they will attend
	#along their journeys. When they picked their staff it will be
	#added to their Thingy basket that is represented with the below
	#dictionary. These things can be put down or can have different values
	#depending on my intentions and user actions..
	Thingy = dict()


	def enter():
		print "Not yet implemented. Subclass it and implement enter() to define functionality."


class Reception(Scene):

	exits = {'left': 'scorpion', 'middle': 'knife', 'right': 'meat'}

	def __init__(self):
		self.Thingy['rec_key'] = False


	def enter(self):

		print "You are in a dark room!"

		if self.Thingy['rec_key'] == True:

			print "You can see three doors:"
			print "left, middle, right!"

		else:

			print "You can see three doors:"
			print "left, middle, right"
			print "and a key on the floor!"

		while True:
#		print "What do you do next?"
			print  ("#"*20)
			print ("You have the following in your basket: %r" % self.Thingy)
			next = raw_input('\nWhat do you do next? |->')

			if 'pick' in next or 'Pick' in next:
				print "Key picked, well done!"
				self.Thingy['ring']= True

			elif self.exits.get(next):
				print (self.exits.get(next))
				return self.exits.get(next)

			else:
				print "I dont't uderstand you, sorry!"
				print "Try something else!"


class MeatRoom(Scene):

	def enter(self):
		print "You're in Meat Room"

		valasz = raw_input('->')
		if valasz == 'I':
			return 'reception'

		else:
			return 'knife' 



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

	def enter(self):
		print "You're dead!"
		exit(1)


class Map(object):

	scenes = {
		'reception': Reception(), 'knife': KnifeRoom(),
		'meat': MeatRoom(), 'scorpion': Scorpions(),
		'diamond': DiamondRoom(),'gold': GoldRoom(),
		'koipond': KoiPondRoom(), 'escape': Escape(), 'dead': Dead()
		}

	def next_scene(self, nxt):
		return self.scenes.get(nxt)

	def start_scene(self):
		return self.scenes.get('reception')

__all__ = [Map]


a = Map()
next = a.next_scene('reception')

while True:

	next_scene = next.enter()
	next = a.next_scene(next_scene)
