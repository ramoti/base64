import base64

def codificar():
    if a == "C":
        texto = input("digite o texto para codificar: ")
        texto_bytes = texto.encode('ascii')
        base64_bytes = base64.b64encode(texto_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(base64_message)

def decodificar():
    if a == "D":
        codigo = input("digite o texto para decodificar: ")
        decodificarBytes = base64.b64decode(codigo)
        decodificarStr = str(decodificarBytes, "utf-8")
        print(decodificarStr)

a = input(str("digite C para codificar ou D para decodificar um texo: "))
codificar()
decodificar()
