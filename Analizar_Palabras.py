def analizar_palabras():
    palabra=raw_input("Introduce una palabra: ")
    longitud=len(palabra)
    print("La palabra "+palabra+" tiene "+str(longitud)+" letras")
    for cont in range(0,longitud):
        print(palabra[cont])
analizar_palabras()
         
