from printing import printc as printc; from printing import printl as printl; from printing import inputl as inputl
from tools import portada as portada; from tools import limpiar as limpiar
from os import system as system

def make_pdf():
	limpiar(); portada()
	printc('Crear PDF'); print()

	ruta = inputl('Ingrese la ruta: ')

	for i in range(1, 2):
		system(f'xelatex -output-directory={ruta} portada/portada.tex')
