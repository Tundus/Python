import sys
sys.path.append('/home/andras/docs/pythonHW/ex48')
sys.path.append('/home/andras/docs/pythonHW/ex49')
from nose.tools import *
from ex48.lexicon import *
from ex49.parser import *

def test_lexicon():
	result = [('verb', 'Go'), ('stop', 'to'), ('noun', 'door')]
	assert_equal(result, scan('Go to door'))

def test_peek():
	word_list = scan('Take second door')
	assert_equal('verb', peek(word_list))
	word_list = []
	assert_equal(None, peek(word_list))

def test_match():
	word_list = scan("Kill the bear")
	expecting = 'verb'
	assert_equal(('verb', 'Kill'), match(word_list, expecting))
	word_list.pop(0)
	skip(word_list, 'stop')
	expecting = peek(word_list)
	assert_equal((expecting, 'bear'), match(word_list, expecting))

def test_skip():
	word_list = scan("to go to to to door")
	skip(word_list, 'stop')
	assert_equal(match(word_list, 'verb'), ('verb', 'go'))

def test_parse_verb():
	word_list = scan("Go to 2 door")
	assert_equal(peek(word_list), 'verb')
	assert_equal(parse_verb(word_list), ('verb', 'Go'))
	#skip(word_list, 'stop')
	assert_raises(ParserError, parse_verb, word_list)

def test_parse_object():
	word_list = scan("to north go door")
	result1 = ('direction', 'north')
	assert_equal(parse_object(word_list), result1)
	#skip(word_list, 'direction')
	result2 = ('verb', 'go')
	assert_equal(parse_verb(word_list), result2)
	#assert_equal(word_list, scan("to north go door"))
	assert_raises(ParserError, parse_verb, word_list)
	result3 = ('noun', 'door')
	assert_equal(parse_object(word_list), result3)

def test_subject():
	word_list = scan("of Go to north")
	#skip(word_list, 'stop')
	#assert_equal(peek(word_list), 'verb')
	#assert_equal(parse_verb(word_list), ('verb', 'Go'))
	result = parse_subject(word_list, ('noun', 'player'))
	assert_equal(result.subject, 'player')
	assert_equal(result.verb.lower(), 'go')

def test_sentence():
	word_list = scan("go to door 3")
	scan('3')
	#assert_equal(parse_number(number_list), 3)
	#assert_equal(parse_verb(word_list), ('verb', 'go'))
	result1 = parse_sentence(word_list)
	assert_equal(result1.verb, 'go')
	assert_equal(result1.object, 'door')
	assert_equal(result1.number, 3)
	word_list2 = scan('hell')
	assert_raises(ParserError, parse_sentence, word_list2)
