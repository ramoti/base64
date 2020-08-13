import base64

a = input(str("digite C para codificar ou D para decodificar um texo: "))

def codificar():
    if a == "C":
        message = input("digite o texto para codificar: ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(base64_message)
codificar()

def decodificar():
    if a == "D":
        encodedStr = input("digite o texto para decodificar: ")
        decodedBytes = base64.b64decode(encodedStr)
        decodedStr = str(decodedBytes, "utf-8")
        print(decodedStr)
decodificar()