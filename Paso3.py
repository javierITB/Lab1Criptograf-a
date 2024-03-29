from scapy.all import *
from collections import Counter
import string

# Frecuencia de las letras en español
frecuencia_espanol = {
    'A': 12.53, 'B': 1.42, 'C': 4.68, 'D': 5.86, 'E': 13.68,
    'F': 0.69, 'G': 1.01, 'H': 0.70, 'I': 6.25, 'J': 0.44,
    'K': 0.02, 'L': 4.97, 'M': 3.15, 'N': 6.71, 'Ñ': 0.31,
    'O': 8.68, 'P': 2.51, 'Q': 0.88, 'R': 6.87, 'S': 7.98,
    'T': 4.63, 'U': 3.93, 'V': 0.90, 'W': 0.01, 'X': 0.22,
    'Y': 0.90, 'Z': 0.52, ' ': 0
}

def descifrar_mensaje(pcap_file):
    # Leer la captura de Wireshark
    paquetes_icmp = rdpcap(pcap_file)

    # Extraer el mensaje cifrado de los paquetes ICMP
    mensaje_cifrado = ""
    for paquete in paquetes_icmp:
        if Raw in paquete:
            datos = paquete[Raw].load.decode('utf-8')
            mensaje_cifrado += datos
        

    # Analizar el mensaje cifrado para todos los corrimientos posibles
    mensaje = ''
    freq = 0
    mensajes = []
    for corrimiento in range(1, 26):
        mensaje_descifrado = ""
        for caracter in mensaje_cifrado:
            if caracter.isalpha():
                codigo = ord(caracter)
                if (codigo - corrimiento)>96:
                    codigo_descifrado = codigo - corrimiento
                else:
                    codigo_descifrado = 26 + codigo - corrimiento
                    
                mensaje_descifrado += chr(codigo_descifrado)
            else:
                mensaje_descifrado += caracter

        numero = 0
        mensaje_descifrado = mensaje_descifrado.upper()
        mensajes.append(mensaje_descifrado)

        for caracter in mensaje_descifrado:
            numero += frecuencia_espanol[caracter]

        if(numero > freq):
            freq = numero
            mensaje = mensaje_descifrado

        
    corrimiento = 1
    for mensa in mensajes:
        # Imprimir el mensaje descifrado y marcar la opción más probable en verde
        if mensa == mensaje:
            print("\033[92m" + f"{corrimiento}\t{mensa}" + "\033[0m")
            
        else:
            print(f"{corrimiento}\t{mensa}")
        
        corrimiento = corrimiento + 1


import sys

if len(sys.argv) != 2:
    print("Uso: python3 Paso3.py <archivo_pcap>")
    sys.exit(1)

pcap_file = sys.argv[1]
descifrar_mensaje(pcap_file)