Juan Jose Gaytan Mertens
David Perez Jacome

El código esta en el archivo CKY.py

Se desarrolló en Eclipse IDE con PyDev sobre Ubuntu

Sobre la gramática asumimos que:

- la primer producción del achivo contiene el símbolo inicial, 
- los símbolos terminales son letras minúsculas
- los símbolos no-terminales son letras mayúsculas
- las producciones están una por linea
- las reglas de produccion están separadas por salto de linea

El programa acepta cadenas de caracteres y, antes de evaluarlas, quita los espacios en blanco y convierte la cadena en formato de minúsculas.

Nuestro mayor problema fue traducir los subíndices de las celdas de la tabla triangular inferior y de las particiones de la cadena que usa algoritmo CKY a subíndices que manejan los arreglos, listas y cadenas de Python.

Los archivos de texto archivo1.txt y archivo2.txt contienen las gramáticas ejemplos que están en alfNota09.pdf y en el video Draft06.FormaNormalChomskyAlgoritmoCKY respectivamente.
