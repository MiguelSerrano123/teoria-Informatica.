def muestra_anteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero-cont)

def muestra_posteriores(numero,correlativo):
    for cont in range(1,correlativo+1):
        print(numero+cont)
                 
def devuelve_numeros():
    numero=input("Dime un numero")
    correlativo=input("Cuantos numeros anteriores y posteriores quieres")
    muestra_anteriores(numero,correlativo)
    muestra_posteriores(numero,correlativo)

devuelve_numeros()
