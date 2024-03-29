import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""
    for caracter in texto:
        # Verificar si el caracter es una letra
        if caracter.isalpha():
            # Obtener el código ASCII del caracter
            codigo = ord(caracter)
            # Verificar si es mayúscula o minúscula
            if caracter.isupper():
                # Aplicar corrimiento a las letras mayúsculas
                codigo_cifrado = (codigo - 65 + corrimiento) % 26 + 65
            else:
                # Aplicar corrimiento a las letras minúsculas
                codigo_cifrado = (codigo - 97 + corrimiento) % 26 + 97
            # Convertir el código ASCII cifrado de nuevo a caracter
            caracter_cifrado = chr(codigo_cifrado)
            texto_cifrado += caracter_cifrado
        else:
            # Conservar caracteres que no son letras
            texto_cifrado += caracter
    return texto_cifrado

if __name__ == "__main__":
    # Obtener los argumentos de línea de comandos
    if len(sys.argv) != 3:
        print("Uso: sudo python3 paso1.py <palabra a cifrar> <corrimiento>")
        sys.exit(1)

    texto_original = sys.argv[1]
    corrimiento = int(sys.argv[2])

    # Cifrar el texto utilizando el algoritmo César
    texto_cifrado = cifrar_cesar(texto_original, corrimiento)

    # Mostrar el texto cifrado
    print(texto_cifrado)
