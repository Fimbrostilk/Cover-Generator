# Print center, right and left of the window
from os import get_terminal_size as t_size

def printc(string):
	print(f'{string:^{t_size().columns}}')

def printl(string):
	print(f'{string:<56}'.center(t_size().columns))

def printr(string):
	print(f'{string:>56}'.center(t_size().columns))

def inputl(string):
	space = ''
	if not (t_size().columns % 2) == 0:
		print(f'{space:{((t_size().columns-56)/2)+1}}{string}', end='')
	else:
		print(f'{space:{((t_size().columns-56)/2)}}{string}', end='')
	return input()

def inputc(string):
	return input(f'{string:>56}'.center(t_size().columns))
