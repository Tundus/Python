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
		raw_tools, room, health = load_data('Player1')

		for k,v in decode_dict(raw_tools).items():
			Scene().Thingy[k] = v
		
		print raw_tools, Scene().Thingy.items(), room
		return self.scenes.get(room)

act_scene = Map().start_scene()

while True:

	nxt_scn = act_scene.enter()
	save_data(encode_dict(Scene().Thingy), nxt_scn, 1000, 'Player1')
	act_scene = Map().next_scene(nxt_scn)

__all__ = [Map]
