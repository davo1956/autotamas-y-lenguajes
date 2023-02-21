'''
Created on 04 dic. 2020

@author: Juan Gaytan

Programa que implementa el algoritmo CKY a partir de una gramática en FNC de un archivo .txt 
y una cadena de texto ingresada desde consola.

El archivo debe tener las producciones por renglon y debe estar en la misma carpeta que el
archivo del código.

'''
import sys
import re

#Arreglo donde guardamos la gramatica del archivo
arreglo = []

#Arreglo donde guardamos la gramática sin caracteres especiales
gramatica = []

def crearMatriz(n):
    '''
    Esta función crea una matriz triangular inferior vacía de tamaño combinación n+1 en 2 
    La matriz tendrá n filas  
    @param n: longitud de la cadena a leer, tipo int
    @return: una matriz de n x m
    '''
    matriz = []
    for i in range(n):
        a = [""]*(i+1)
        matriz.append(a)
    return matriz

def quitarEspacios(cadena):
    '''
    Esta función quita saltos de linea, tabulaciones y espacios en blanco de una cadena de texto
    '''
    cadena = cadena.replace(" ","")
    cadena = cadena.replace("\t","")
    cadena = cadena.replace("\n","")
    return cadena 

def imprimeTabla(tabla):
    '''
    Esta función imprime en consola la tabla T triangular inferior
    @param tabla: la tabla de variables V
     '''     
    numero = 0
    print(" ",numero)
    for row in tabla:
        numero += 1
        print(row,numero)
    return

# Inicio del programa

print("Programa que implementa el algoritmo CKY a partir de una GFNC y una cadena")
print("\nFavor de indicar el nombre del archivo con su extensión: ", end="")
nombreArchivo = input()

nombreArchivo = quitarEspacios(nombreArchivo)

try:
    try:
        with open(nombreArchivo) as f:
            archivo = f.readlines()
    except IOError as e:
        print("Archivo no existe")
        sys.exit()
except Exception as e:
    print(str(e))
    sys.exit()

# Representación inicial del programa

for row in archivo:
    arreglo.append(row)

print("Cadena a leer: ", end="")
cadena = input()
cadena = quitarEspacios(cadena)
cadena = cadena.lower()


print("\nLa GFNC es: \n")

for row in arreglo:
    print(row)

#Este for lee la produccion S y la almacena en el arreglo gramatica_valor_inicial

for i in range(len(arreglo)):
    gramatica.append(re.findall(r'\w', arreglo[i]))  

tablaT = crearMatriz(len(cadena))

print("\nA continuación la posible derivacion: ")

imprimeTabla(tablaT)

# Primera parte del algoritmo CKY
for caracter in range(len(cadena)):                                 #Para cada elemento de la cadena
    for renglon in gramatica:                                       #Para cada renglón de la producción, (cada renglón es una producción)
        if cadena[caracter:caracter+1] in renglon:                  #Si el caracter de la cadena está en el renglon del arreglo gramática
            tablaT[caracter][len(tablaT[caracter])-1]= tablaT[caracter][len(tablaT[caracter])-1] + renglon[0]    #Se añade la variable al último elemento del renglón # caracter de la tabla triangular  

imprimeTabla(tablaT)

#Segunda parte del algoritmo CKY
for tamanoSubCadena in range(2,len(cadena)+1,1):                  # Para cada longitud >= 2 hasta el tamaño de la cadena mas 1
    j = tamanoSubCadena
    for i in range(len(cadena)-1):                                # Para cada subcadena de tamaño 
        #print("W[",i,"][",j,"]")                                 # Son para lectura referencia y traducir la coordenada de la tabla contra la coordena del arreglo
        #tablaT[j-1][i] = "["+str(j-1)+","+str(i)+"]"
        for otro in range(tamanoSubCadena-1):                     # Para cada combinación de cadenas de i a j
            #print("\tW",i,",",i+1+otro,"+ W",i+1+otro,",",j)     # Lectura referencia
            w1 = tablaT[i+1+otro-1][i]                            # Toma las variables de cada celda y las guarda en dos cadenas
            w2 = tablaT[j-1][i+1+otro]
            for produccion in gramatica:                          # Busca en todas las producciones de la gramática
                if w1 != "" and w2 != "":                         # Si las variables no son vacias procede                 
                    if len(produccion) == 3:                      # Toma solo las producciones de longitud 3 ya que de menor tamaño son de la forma A -> a
                        for simbolo1 in w1:                       # Compara cada simbolo de la cadena w1 contra cada simbolo de la cadena w2
                            for simbolo2 in w2:
                                if simbolo1 == produccion[1] and simbolo2 == produccion[2]: # Verifica si los simbolos de las variables están del lado derecho de la produccion en turno
                                    tablaT[j-1][i] = tablaT[j-1][i] + produccion[0]         # Si lo están ambos entonces añade la variable del lado izquierdo de la producción                                                   
        j += 1
        if j > len(cadena):
            break
    imprimeTabla(tablaT)

print("\n\nResultado:")
if gramatica[0][0] in tablaT[len(cadena)-1][0]:
    print("La cadena ",cadena,"si pertenece a L(G)\n")
else:
    print("La cadena ",cadena,"no pertenece a L(G)\n")

imprimeTabla(tablaT)

