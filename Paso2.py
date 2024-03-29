
from curses import raw
from os import wait
import random
import sys
from time import sleep
from scapy.all import ICMP, IP, send

def enviar_paquete_icmp(destino, caracter, contador):
    
    
    
    # Convertir el contador a hexadecimal
    contador_hex = hex(contador)[2:].zfill(4)
    
    # Extraer los bytes del contador
    contador_bytes = bytes.fromhex(contador_hex)
    
    # Reemplazar el último byte con el caracter
    caracter_codificado = contador_bytes[:] + bytes([caracter])+ bytes.fromhex('101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637')

    paquete_icmp = IP(dst=destino)/ICMP(id=0x000c, seq = contador)/ICMP(id=0x0c00, seq=contador)/caracter_codificado
    
    # Enviar el paquete ICMP
    send(paquete_icmp, verbose=False)
    sleep(1)

def enviar_texto_icmp(destino, texto):
    # Generar un número ascendente semi-aleatorio para el contador
    contador = random.randint(1, 10)
    for caracter in texto:
        print(".")
        # Convertir el caracter a su valor ASCII
        valor_ascii = ord(caracter)


        # Enviar el valor ASCII como un paquete ICMP
        enviar_paquete_icmp(destino, valor_ascii, contador)
        
        print("sent 1 packet.")
        contador+=1

if __name__ == "__main__":
    # Verificar si se proporciona la frase como argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Uso: sudo python3 paso2.py <frase a enviar>")
        sys.exit(1)

    # Dirección IP de loopback para evitar tráfico malicioso
    destino = "127.0.0.1"
    
    # Obtener la frase a enviar desde los argumentos de línea de comandos
    texto_a_enviar = sys.argv[1]
    
    # Enviar cada caracter de la frase en un paquete ICMP
    enviar_texto_icmp(destino, texto_a_enviar)
