from os import get_terminal_size as t_size; from os import system as system; from os import name as name
from printing import printc as printc; from printing import inputl as inputl; from printing import inputc as inputc

def portada():
	printc('┌────────────────────────────────────────────────────────┐')
	printc('│ » Instituto Politécnico Nacional                       │')
	printc('│ » Escuela Superior de Ingeniería Mecánica y Eléctrica  │')
	printc('│   Unidad Profesional Zacatenco (ESIMEZ)                │')
	printc('│ » Ingenieria en Comunicaciones y Electrónica           │')
	printc('│ » Portuguez Padrón Angel - 2025300015                  │')
	printc('└────────────────────────────────────────────────────────┘')

def limpiar():
	system('clear' if name == 'posix' else 'cls')

def entero(mensaje = 'Ingrese un número entero: ', align = 0):
	while True:
		try:
			if align == 'l':
				return int(inputl(mensaje))
			elif align == 'c':
				return int(inputc(mensaje))
			elif align == 0:
				return int(input(mensaje))
		except ValueError:
			pass
