def Analizador_Frases():
    frase=raw_input("dime una frase ")
    print("El texto tiene" + str(len(frase)) + "caracteres")
    letra=""
    cont=0
    for letra in texto:
        cont=cont+1
        print("letra= "+letr+" "+str(cont))
    
Analizador_Frases()
