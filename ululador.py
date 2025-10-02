#ejercicio que lee una palabra y sustituye las vocales por "u"
def ululador():
    vocales="aeiouAEIOU"
    frase_entrada=raw_input("Di algo: ")#lee una palabra
    frase_salida="" #creo una cadena vacia
    for cont in range(0,len(frase_entrada)):
        if(frase_entrada[cont] in vocales): #si la letra que toca es la 'a' concateno una 'u'
            frase_salida=frase_salida+'u'
        else:
            frase_salida=frase_salida+frase_entrada[cont] #concateno la misma letra
    print(frase_salida)
ululador()
