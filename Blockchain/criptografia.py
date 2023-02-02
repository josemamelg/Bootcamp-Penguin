from hashlib import sha256
import json

data = "haupei"
data2 = "hauupei"
data3 = "haupei"
criptado = sha256(data3.encode()) #Siempre usar .encode en string
print(criptado.hexdigest())

#Dato a encriptar
bloque ={
   
    'index' : 1,
    'dato' : "Josema a Luchi 10btc",
    'nonce' : 0
    
}


#Convertir diccionario bloque en string

bloque_string = json.dumps(bloque, sort_keys=True)
criptado2 = sha256(bloque_string.encode())
print(criptado2.hexdigest())




while True:
    bloque['nonce'] += 1
    bloque_string = json.dumps(bloque, sort_keys=True)
    criptado2 = sha256(bloque_string.encode()).hexdigest()
    print(criptado2)
    print(bloque['nonce'])
    if criptado2.startswith("0000"):
        break
    


