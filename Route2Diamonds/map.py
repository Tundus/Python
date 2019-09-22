#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were only included as 
#a salute for Zed Shaw.

class Scene(object):

	def enter():
		print "Not yet implemented. Subclass it and implement enter() to define functionality."


class Reception(Scene):

	def enter(self):
		print "This is Reception Room!"
		return 'meat'

class MeatRoom(Scene):

	def enter(self):
		print "You're in Meat Room"
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
