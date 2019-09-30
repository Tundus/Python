#This is the main module that will operate subordinate modules
from scene import *
from map import *
from db_connect import *

class Engine():

	def play(self):

		Load_tools()
		act_scene = Map().start_scene()

		while True:
			nxt_scn = act_scene.enter()
			if nxt_scn != 'dead':
				save_data(encode_dict(Scene().Thingy), nxt_scn, 1000, 'Player1')
			act_scene = Map().next_scene(nxt_scn)

if __name__ == '__main__':
	game = Engine()
	game.play()


