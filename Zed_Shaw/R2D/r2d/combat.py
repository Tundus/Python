#This is the combat engine
from random import *

def combat_engine(g_func):

	def inner(*f_args):
		comp_result = g_func(*f_args)
		return comp_result

	return inner


def double_dice(x,  y):
	return randint(x,y) + randint(x,y)

def single_dice(x, y):
	return randint(x, y)

def double_dice_2numbers(x, y):
	return randint(x, y), randint(x, y)

#a = combat_engine(double_dice_2numbers)
#print a(1,6)
