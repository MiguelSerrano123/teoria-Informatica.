#ejercicio que lee una palabra y sustituye las vocales por "u"
def ululador():
    vocales_min="aeiou"
    vocales_may="AEIOU"
    frase_entrada=raw_input("Di algo: ")#lee una palabra
    frase_salida="" #creo una cadena vacia
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont] in vocales_min): #si la letra que toca es "vocal" concateno una 'u'
            frase_salida=frase_salida+'u'
        if(frase_entrada[cont] in vocales_may):
            frase_salida=frase_salida+'U'
        else:
            frase_salida=frase_salida+frase_entrada[cont] #concateno la misma letra
    print(frase_salida)
ululador()
