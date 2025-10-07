def Analizador_Frases():
    frase=raw_input("dime una frase ")
    print("El texto tiene " + str(len(frase)) + " caracteres")
    letra=""
    espacio=" "
    cont=0
    num_vocales=0
    num_consonantes=0
    num_de_o=0
    contador_o="oO"
    vocales="AEIOUaeiou"
    palabras=frase.split()
    num_palabras=len(palabras)
    for letra in frase:
        cont=cont+1
        print("letra= "+letra+" "+str(cont))
        if letra in espacio:
            num_consonantes=num_consonantes-1
        if letra in vocales:
            num_vocales=num_vocales+1
        else:
            num_consonantes=num_consonantes+1
        if letra in contador_o:
            num_de_o=num_de_o+1
            
    print("Numero de Vocales:",num_vocales)
    print("Numero de Consonantes:",num_consonantes)
    print("Numero de Palabras:",num_palabras)
    print("Numero de O:",num_de_o)
    
    
    
Analizador_Frases()
