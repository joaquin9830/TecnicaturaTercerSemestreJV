# Para abrir un archivo primero declaramos una variable:
try:
    archivo = open('prueba.txt', 'w', encoding='utf8') # La w es de wite que significa escribir
    archivo.write('\nProgramamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: acción, ejecución y producción\n')
    archivo.write('Las letras son:\na: append  \nw: write  \nr: read  \nx: crear archivo especificado  \n')
    archivo.write('t: para texto o text, \nb: para binario o texto, \nw+: lee y escribe, \nr+: lee y escribe igual a w\n')
    archivo.write('Saludos a todos los pibes de la tecnicatura\n')
    archivo.write('Con esto terminamos\n')
except Exception as e:
    print(e)
finally:
    archivo.close() # SIEMPRE SE DEBE CERRAR CON .CLOSE()

#archivo.write('Todo quedó joya compadre'): Este es un error
