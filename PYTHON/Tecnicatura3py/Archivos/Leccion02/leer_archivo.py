# Modo para leer:
# R de "Leer"

archivo = open('prueba.txt', 'r', encoding='utf8') #Las letras son r read, a append, w write
# print(archivo.read())
# print(archivo.read(16))
# print(archivo.readline())
# print(archivo.readline())

#Vamos a iterar el archivo, cada una de las líneas
#for linea in archivo:
#   print(linea)

archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar archivos')