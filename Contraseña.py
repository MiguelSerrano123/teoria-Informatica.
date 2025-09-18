def generador_contrasena():
    nombre=raw_input("Nombre:")
    apellido1=raw_input("Primer Apellido:")
    apellido2=raw_input("Segundo Apellido:")
    anio=raw_input("Anio en el que naciste:")
    codigo=nombre[:3]+apellido1[:3]+apellido2[:3]+anio[2:4]
    print("tu contrasena es:" , codigo)

generador_contrasena()

    
                      
                    
    
    
