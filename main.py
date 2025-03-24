from os import system as system; from os import name as name
from getch import getch as getch
from printing import printc as printc; from printing import printl as printl
from edit_data import edit_data as edit_data
from make_pdf import make_pdf as make_pdf
from tools import limpiar as limpiar; from tools import portada as portada

def menu():
	printc('Generador de Portadas'); print()
	printl('a) Editar datos')
	printl('b) Crear pdf')
	printl('s) Salir')

while True:
	limpiar(); portada()
	menu()

	match getch():
		case 'a':
			edit_data()
			printl('Intro para terminar...'); getch()
		case 'b':
			make_pdf()
			printl('Intro para terminar...'); getch()
		case 's':
			limpiar(); break
		case _:
			pass
