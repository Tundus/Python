#This is the main module that will operate subordinate modules
from map import Map

class Engine():

	def play(self):
		a = Map()
		next_ready = a.start_scene()

		while True:
			load_next = next_ready.enter()

			next_ready = a.next_scene(load_next)

game = Engine()
game.play()


