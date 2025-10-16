def Menu():
    # MENU
    print("Elige una opcion (1-6): ")
    print("1. Contar el numero de letras")
    print("2. Contar el numero de consonantes")
    print("3. Contar el numero de vocales")
    print("4. Contar el numero de palabras")
    print("5. Contar el numero de de veces que aparece la letra o")
    print("6. Encriptar el mensaje")

def Contar_Caracteres(frase):
    print("Tiene "+str(len(frase))+" caracteres")

def Contar_Vocales(frase):
    vocales="AEIOUaeiou"
    num_vocales=0
    numeros="123456789"
    letra=""
    for letra in frase:
        if(letra in vocales):
            num_vocales=num_vocales+1
    print("Tiene "+str(num_vocales)+" vocales")

def Contar_Consonantes(frase):
    num_consonantes=0
    for letra in frase:
        if(not((letra in vocales) or (letra==" ") or (letra in numeros)))
            num_consonantes=num_consonantes+1
    print("Tiene "+str(num_consonantes)+" consonantes")

def Contar_Palabras(frase):
    num_palabras=0
    for letra in texto:
        if(letra==" "):
            num_palabras=num_palabras+1
    print("Tiene "+str(num_palabras+1)+" Palabras")

def Contar_O(frase):
    num_O=0
    for letra in frase:
        if letra=="o" or letra=="O"):
            num_O=num_O+1
    print("Tiene "+str(num_O)+" O"


def Analizador_Frases():
    #Pido el texto
    frase=raw_input("Introduce una frase: ")
    menu()
    opcion=input("ELIGE UNA OPCION (1-6): ")
    if(opcion==1):
        Contar_Caracteres(frase)
    if(opcion==2):
        Contar_Consonantes(frase)
    if(opcion==3):
        Contar_Vocales(frase)
    if(opcion==4):
        Contar_palabras(frase)
    if(opcion==5):
        Contar_O(frase)
    if(opcion==6):
        encriptar(texto)
   
Analizador_Frases()

