from time import time
import json
from hashlib import sha256
class Bloque():
    def __init__(self, index, transacciones, timestamp, nonce):
        self.index = index
        self.transacciones = transacciones
        self.timestamp = timestamp
        self.bloque_genesis()
        self.nonce = nonce

bloque = Bloque(1, 'Hola', time())
print(bloque.__dict__)

def bloque_genesis(self):
    genesis = Bloque(0, ["Genesis"],time() )
    self.cadena.append(genesis)

@property
def ultimo_bloque(self):
    return self.cadena[-1]

@staticmethod
def criptar():
    bloque_string = json.dumps(bloque,__dict__, sort_keys=True)
    return sha256(bloque_string.encode().hexdigest)

dificultad = 4

def prueba_de_trabajo(self,bloque):
    bloque.nonce = 0

    criptado = self.criptar(bloque)
    while not criptado.startswith("0"*self.dificultad):
        bloque.nonce += 1
        criptado = self.criptar(bloque)
    return criptado

def agregar_transacciones(self, transacciones):
    self.transacciones_pendientes.append(transacciones)

def agregar_bloque(self, bloque, prueba):
    hash_anterior = self.ultimo_bloque.hash
    self.cadena.append(bloque)

def cerrar_bloque(self):
    ultimo_bloque = self.ultimo_bloque
    nuevo_bloque = Bloque(ultimo_bloque.index + 1 , self.transacciones_pendientes, timestamp=())
    self.agregar_bloque(nuevo_bloque)
    self.transacciones_pendientes = []


