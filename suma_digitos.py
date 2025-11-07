def suma_digitos():
    numero=raw_input("Dime un numero ")
    suma=0
    for digito in numero:
        suma=suma + int(digito)
    print("la suma de los digitos es", suma)
suma_digitos()
