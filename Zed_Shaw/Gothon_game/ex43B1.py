from sys import exit
from random import randint
from operator import eq, ne




class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n-----------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mum would be proud...if you were smarter.",
		"Such a looser.",
		"I hava a small puppy that's better at this!"]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal \#25 have invaded your ship and desroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "Your're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume "
		print "flowing around his hate filled body. He is blocking the door to the "
		print "Armory and about to pull a weapon to blast you."

		action = raw_input('|->')

		if action == "shoot":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws "
			print "off your aim. Your laser hits his costume but misses him entirely. This "
			print "completely ruins his brand nen costume his mother bought him, which "
			print "makes him fly into rage and blast you repeatedly in the face until "
			print "until you are dead. Then he eats you."
			return "death"

		elif action == "dodge":
			print "Like a world class boxer you dodge, weave, slip and slide right "
			print "as the Gothon's blaster cranks a laser past your head ."
			print "In the middle of your artful dodge your foot slips and you "
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on  "
			print "your head and eats you."
			return "death"

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughning and can't move."
			print "While laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return "laser_weapon_armory"
		else:
			print "Doesn't compoute!"
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive roll into the weapon armory, crouch and scan the room"
		print "for more Gothons that might be hiding. It's dead quiet, too quiet."
		print "You stand up and run to the far side of the room and find "
		print "a neutron bomb in its container. There is a keypad lock on the box."
		print "and you need the code to get the bomb out. If you get the code "
		print "wrong 10 times then the lock closes forever and you can't "
		print "get the bomb. The code is 3 digits."

		code = "%d%d%d" % (randint(1,9), randint(0,9), randint(0,9))
		guess = guesses = 0

		while guesses < 10:

			try:
				guess = int(raw_input("[keypad. guesses left %i]>" % (10-guesses)))
				if len(str(guess)) != 3:
					raise InputLengthError()

			except ValueError as inst:
				print "Numbers only please!" #inst.args

			except InputLengthError:
				print "THREE digits, remember?!"

			else:
				if guess == 999 or guess == int(code):
					code = guess
					break
				else:
					print "BZZZZZEEDDDD"

			guesses += 1
#			print "repr(guess): %r, int(999): %i, repr(code): %r, guess=cheat?: %r)" % (guess, int(999), code, eq(int(guess), 999))

		if guess == code:
			print "The container click open and the seal breaks, letting gas out."
			print "You grab the neutron bomb and run as fast as you can to the"
			print "bridge where you must place it in the right spot."
			return ["the_bridge", "popup_room"][randint(1,1)]

		else:
			print "The lock buzzes one last time and then you hear a sickening "
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship and you die."
			return "death"


class TheBridge(Scene):

	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
            	print "under your arm and surprise 5 Gothons who are trying to"
            	print "take control of the ship.  Each of them has an even uglier"
            	print "clown costume than the last.  They haven't pulled their"
            	print "weapons out yet, as they see the active bomb under your"
            	print "arm and don't want to set it off."

		action = raw_input('|->')

            	if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door.  Right as you drop it a"
			print "Gothon shoots you right in the back killing you."
			print "As you die you see another Gothon frantically try to disarm"
			print "the bomb. You die knowing they will probably blow up when"
			print "it goes off."
			return 'death'

		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "and the Gothons put their hands up and start to sweat."
			print "You inch backward to the door, open it, and then carefully"
			print "place the bomb on the floor, pointing your blaster at it."
			print "You then jump back through the door, punch the close button"
			print "and blast the lock so the Gothons can't get out."
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'

		else:
			print "Doesn't compute!"
			return 'the_bridge'


class EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"

		good_pod = randint(1,2)

		while True:
			try:
				guess = int(raw_input("[pod \#]> "))
				if guess > 5:
					raise InputLengthError()

			except ValueError as inst2:
				print "Input error!" #, inst2.args

			except InputLengthError:
				print "There are FIVE pods only!" 

			else:
				break

		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'

		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below.  As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time.  You won!"
			exit (1)


class PopUpRoom(Scene):

	def enter(self):

		print "While leaving the room a massive electric outburst"
		print "shakes the whole ship. The unimaginable amount of" 
		print "energy creates a wormhole and you step right into it."
		print "Surprisingly, it teleports you to the storage room!"
		print "Less surprisingly you face the biggest and ugliest Gothon you've"
		print "ever met. You both reach for your laser weapons at the same time."

		fight = Battle_Engine()
		return fight.play('Blondy', 'Gothon', 'double_dice')


class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'popup_room': PopUpRoom()
		}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


class Game(object):
	print "Not yet implemented!"

class DoubleDiceCast(Game):

	def __init__(self):
		pass 

	@staticmethod
	def value_func(x, y):
		return randint(x, y) + randint(x, y)

	def game_on(self, player, alien):

			self.alien = alien
			self.player = player

			self.score_player_func = compute_score(DoubleDiceCast().value_func)
			self.score_player = self.score_player_func(1, 6)

			self.score_alien_func = compute_score(DoubleDiceCast().value_func) 
			self.score_alien = self.score_alien_func(1, 6)

			print "\nHello %s! I am a battle engine!" % self.player 
			print "\nThe outcome of your duel with the %s will be decided by" % self.alien
			print "a single throw with two dice."
			print "The %s has started and achieved: %i!" % (self.alien, self.score_alien)
			print "Can you beat that?"
			print "Hit a button to reveal your faith!"

			x = raw_input('?')

			if  self.score_player > self.score_alien:
				print "You splashed them onto the table to score"
				print "a total of %i! Well done! You can carry on" % self.score_player
				print "with your journey! The wormhole is still"
				print "open..."
				return "the_bridge"

			elif self.score_player == self.score_alien:
				print "You splashed them onto the table to score"
				print "a total of %i!" % self.score_player
				print "Well, that is technically a tie but since the %s" % self.alien
				print "began the lap it goes to you! Well done!"
				print "You can carry on with your journey!"
				print "The wormhole is still open..."
				return "the_bridge"

			else:
				print "You knew that your chances are to beat that score!"
				print "Well, you fearlessly cast the dice...to achieve %i points," % self.score_player
				print "which is not enough! Sorry!"
				return "death"

def compute_score(func):

	def wrapper(*args, **kwargs):
		score = func(*args, **kwargs)
		return score
	return wrapper

class Battle_Engine(object):

	games2play = {'double_dice': DoubleDiceCast()
			}

	def play(self, player, alien, game):

		self.play_game = Battle_Engine.games2play.get(game)
		return self.play_game.game_on(player, alien)

class MyError(Exception):
	"""Base class for exception in this module"""
	pass


class InputLengthError(MyError):
	"""Raised when number entered by user is too short or too long"""
	"""Base class for exception in this module"""
	pass


a_map = Map('central_corridor')  
a_game = Engine(a_map)
a_game.play()

