def Curvi():
    Palabra=raw_input("Dime una palabra ")
    Letras_Curvas="QRUOPSDGJÑCB"
    Contar_Curvas=0
    for cont in Palabra:
        if cont in Letras_Curvas:
            Contar_Curvas=Contar_Curvas+1
        else:
            Contar_Curvas=Contar_Curvas+0

    print("La palabra",Palabra,"tiene",Contar_Curvas,"Letras curvas")
Curvi()
