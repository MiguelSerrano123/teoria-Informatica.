def programa_1():
    max_num = float(input("Introduce un número: " ))
    sum_nums = max_num
    anterior=max_num
    creciente=True
    cont=1
    while cont < 10:
        num = float(input("Introduce otro número "))
        sum_nums =sum_nums+ num
        if num > max_num:
            max_num = num
        if num <= anterior:
            creciente=False
        anterior=num
        cont=cont+1
    print("The largest number is:",max_num )
    print("The average is:",sum_nums/10 )

    if creciente == True:
        print("Los numeros son Crecientes")
    if creciente == False:
        print("Los numeros no son Crecientes")
programa_1()
