#This is our Map module with every scene/room in this game.
#Scene() classes should come first as Map() class will need to know about them.
#Recent scenes/rooms are: Reception, Meat, Knife, Scorpion, Diamond, 
#Gold, KoiPond, Escape, Dead. Gold and KoiPond were included for  
#saluting Zed Shaw.

from collections import defaultdict
from scene import *
from db_connect import *

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
		tools, room, health = load_data('Player1')
		return self.scenes.get(room)
