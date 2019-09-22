from string import punctuation, whitespace, digits
from random import randint
from bisect import bisect_left

def process_file(filename):
	h = dict()
	fp = open(filename)
	for line in fp:
		process_line(line, h)
	return h

def process_line(line, h):
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(punctuation + whitespace + digits)
		word = word.lower()
		if word != '':
			h[word] = h.get(word, 0) + 1

hist = process_file('emma.txt')

def cum_sum(list_of_numbers):
	cum_list = []
	for i, elem in enumerate(list_of_numbers):
		if i == 0:
			cum_list.append(elem)
		else:
			cum_list.append(cum_list[i-1] + elem)
	return cum_list

def random_word(h):
	word_list = list(h.keys())
	num_list = []
	for word in word_list:
		num_list.append(h[word])
	cum_list = cum_sum(num_list)
	i = randint(1, cum_list[-1])
	pos = bisect_left(cum_list, i)
	return word_list[pos]

print(random_word(hist))
