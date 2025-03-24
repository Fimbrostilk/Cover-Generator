from printing import printc as printc; from printing import printl as printl; from printing import inputl as inputl
from tools import portada as portada; from tools import limpiar as limpiar; from tools import entero as entero
import json

def edit_data(): # Función que permite editar los datos de la portada
	limpiar(); portada()
	printc('Editar datos'); print()

	with open('datos.json', 'r') as archivo: # Cargar el diccionario con los datos de la portada
		datos = json.load(archivo); archivo.close()

	for dato in datos: # Modificar datos
		if dato == 'nombres':
			no_integrantes = entero('Ingrese el número de participantes: ', 'l')
			if no_integrantes == 1: # Solo un autor
				value = inputl(f'Ingrese el nombre: ')
				datos.update({dato: value})
			else: # Integrantes de un equipo
				integrantes = []
				no_equipo = entero('Ingrese el número de equipo (-1 si no se desea implementar): ', 'l')
				for i in range(no_integrantes):
					integrantes.append(inputl(f'Ingrese integrante {i+1}: '))
				datos.update({dato: integrantes})
		else: # Demas datos de la portada
			value = inputl(f'Ingrese {dato}: ')
			datos.update({dato: value})

	with open('datos.json', 'w') as archivo: # Escribir el nuevo diccionario
		archivo.write(json.dumps(datos, indent=4)); archivo.close()

	with open('portada/datos.tex', 'w') as archivo: # Modificar el .tex
		contenido = ''

		for dato in datos:
			if (dato == 'nombres') and (no_integrantes == 1): # Solo para un integrante
				contenido += '\\newcommand{\\nombres}{\\large{\\textbf{Alumno:} ' + f'{datos.get(dato)}' + '}}\n'
			elif (dato == 'nombres') and (no_integrantes != 1): # Crear itemize en LaTeX
				contenido += '\\newcommand{\\nombres}{\n'
				if no_equipo == -1:
					contenido += '\\large{\\textbf{Integrantes: }}\n'
				else:
					contenido += '\\large{\\textbf{Equipo ' + f'{no_equipo}' + ' - Integrantes: }}\n'
				contenido += '\\begin{itemize}\n'
				for i in range(no_integrantes): # Crear los items con los nombres de los integrantes
					contenido += f'\t\\item {datos[dato][i]}'
				contenido += '\\end{itemize}}'
			else:
				contenido += '\\newcommand{\\' + f'{dato}' + '}{' + f'{datos.get(dato)}' + '}\n'

		archivo.write(contenido); archivo.close()
