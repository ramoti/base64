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

########################################################################################################

import base64

def main () : 

    opcao = input(str("digite C para codificar ou D para decodificar um texo: "))

    if opcao == "C":
        palavra_a_ser_codificada = input("Digite a frase/palavra que desejas codificar: ")
        codificar_frase(palavra_a_ser_codificada)

    elif opcao == "D": 
        palavra_a_ser_decodificada = input("Digite a frase/palavra que desejas decodificar: ")
        decodificar_frase(palavra_a_ser_decodificada)

def codificar_frase(palavra_a_ser_codificada):

    texto_bytes = palavra_a_ser_codificada.encode('ascii')
    base64_bytes = base64.b64encode(texto_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    return (base64_message)

def decodificar_frase(palavra_a_ser_decodificada):

    decodificarBytes = base64.b64decode(palavra_a_ser_decodificada)
    decodificarStr = str(decodificarBytes, "utf-8")
    print(decodificarStr)
    return (decodificarStr)

if __name__ =='__main__':
    main ()
