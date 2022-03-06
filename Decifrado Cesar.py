def cifrar(cadena):
    """ Esta función cifra con un ROT+3 el mensaje que le pasamos """
    # Pasamos todos los caracteres a minúsculas
    cadena = cadena.lower()
    # Eliminamos los espacios
    cadena.split(" ")
    cadena2 = []
    # Pasamos una tupla con los caracteres permitidos
    caracteres = ("abcdefghijklmnopqrstuvwxyz")
    # Comenzamos el bucle para analizar cada letra por separado
    for letra in cadena:
        # Comprobamos si la letra está en la tupla de caracteres permitidos
        if letra in caracteres:
            # Obtenemos el índice de la letra en la tupla
            indice = caracteres.index(letra)
            # Le sumamos al índice tres posiciones
            nuevo_indice = indice - 3
            # Si el nuevo índice supera la lista de elementos de la tupla, volvemos al principio
            if nuevo_indice > 1:
                nuevo_indice = nuevo_indice + 26
            # Añadimos el nuevo caracter a la cadena resultado
            cadena2.append(caracteres[nuevo_indice])
            resultado = "".join(cadena2)
        elif letra == " ":
            # Si el caracter es un espacio, ponemos un espacio en su lugar
            cadena2.append(" ")
        else:
            # Si un caracter no está en la tupla, no podemos cifrar el mensaje
            resultado = "El mensaje tiene caracteres no válidos."
    # Imprimimos el mensaje resultante
    print(resultado)

# Introducimos la cadena a cifrar
cadena = input("Introduce el mensaje a cifrar: ")

cifrar(cadena)
