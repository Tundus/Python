direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back', 'middle', 'left', 'right']
verbs = ['go', 'stop', 'kill', 'eat', 'open', 'take', 'drop', 'walk', 'pick']
stops = ['the', 'in', 'of', 'from', 'at', 'it', 'to']
nouns = ['door', 'bear', 'princess', 'cabinet', 'key']
d = {'direction': direction, 'verb': verbs, 'stop': stops, 'noun': nouns}

def stack():
	joint_dict = {}
	for k, v in d.items():
		res =  (dict.fromkeys(v, k))
		joint_dict.update(res)
	return joint_dict

#stack = {dict.fromkeys(v,k) for k,v in d.items()}
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

glob_dict = stack()

def scan(user_input):
	lexikon = []

	for relem in user_input.split():
		elem = relem.lower()
		if convert_number(elem) == None:
			type = glob_dict.get(elem, 'error') 
			tw = type, relem
		else :
			tw = 'number', convert_number(elem)

		lexikon.append(tw)

	return lexikon
