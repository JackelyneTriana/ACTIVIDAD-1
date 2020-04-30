import pandas as pd

nombres = {}
separador = ("*" * 40)
validador = False
archivoTexto2 = open("Reporte.txt","w")

def menu():
    print("1) Capturar 30 estudiantes")
    print("2) Capturar las calificaciones de los 30 estudiantes")
    print("3) Consultar las materias con menor rendimiento")
    print("4) Consultar los estudiantes con mas de 2 materias reprobadas")
    respuesta = int(input("Elige la opcion del menu que desees:"))
    print(separador)
    while type(respuesta) != int:
        respuesta = int(input("Opcion invalida, teclea una opcion del menu"))
    if respuesta == 1:
        Opcion_1()
    elif respuesta == 2:
        if nombres == {}:
            print("Debes capturar primero los estudiantes en la opcion 1 del menu")
            menu()
        else:
            Opcion_2()
    elif respuesta == 3:
        if nombres == {}:
            print("Debes capturar primero los estudiantes en la opcion 1 del menu")
            menu()
        elif validador == False:
            print("Debes capturar las calificaciones de los estudiantes en la opcion 2 del menu")
            menu()
        else:
            Opcion_3()
    elif respuesta == 4:
        if nombres == {}:
            print("Debes capturar primero los estudiantes en la opcion 1 del menu")
            menu()
        elif validador == False:
            print("Debes capturar las calificaciones de los estudiantes en la opcion 2 del menu")
            menu()
        else:
            Opcion_4()
    else:
        Opcion5()
        

def Opcion_1():
    print("INGRESE LOS NOMBRES DE 30 ALUMNOS")
    registros_cant = 1
    while registros_cant <= 30:
        nombre = input("dame el nombre de un alumno: ")
        nombres[nombre]= ""
        registros_cant = registros_cant + 1
    print("ALUMNOS REGISTRADOS CORRECTAMENTE")
    for x in nombres:
        print(x)
    print(separador)
    menu()

def Opcion_2():
    global validador
    validador = True
    calificaciones= []
    for x in nombres:
        print(f"INGRESA LAS CALIFICACIONES DE {x}: ")
        calificaciones.append(int(input("Programacion: ")))
        calificaciones.append(int(input("Base de datos: ")))
        calificaciones.append(int(input("Macroeconomia: ")))
        calificaciones.append(int(input("Estadistica: ")))
        calificaciones.append(int(input("Contabilidad: ")))
        nombres[x] = calificaciones
        calificaciones = []
    registros = pd.DataFrame(nombres)
    registros.index = ["Programacion", "Base de datos", "Macroeconomia", "Estadistica", "Contabilidad" ]
    print(separador)
    print("CALIFICACIONES AGREGADAS CORRECTAMENTE")
    print(registros.T)
    print(separador)
    menu()
    
def Opcion_3():
    registros = pd.DataFrame(nombres)
    registros.index = ["Programacion", "Base de datos", "Macroeconomia", "Estadistica", "Contabilidad" ]
    print(f"PROMEDIO POR MATERIA:\n{registros.T.mean()}")
    media=registros.T.mean()
    registro=str(media)

    archivoTexto2.write("PROMEDIO POR MATERIA \n")
    archivoTexto2.write(registro)
    archivoTexto2.write("\nEl PROMEDIO DE LA MATERIA CON MENOR RENDIMIENTO ES: ")
    
    registros = pd.DataFrame(nombres)
    registros.index = ["Programacion", "Base de datos", "Macroeconomia", "Estadistica", "Contabilidad" ]
    print(f"PROMEDIO POR MATERIA:\n{registros.T.mean()}")
    asignatura_masbaja = min(registros.T.mean())
    
    print("EL PROMEDIO DE LA MATERIA CON MENOR RENDIMIENTO ES: \n")
    print(asignatura_masbaja)
    asignaturaMasBaja = min(registros.T.mean())
    asignaturaBaja =str(asignaturaMasBaja)
    archivoTexto2.write(asignaturaBaja)
    print(separador)
    menu()


def Opcion_4():
    registros = pd.DataFrame(nombres)
    registros.index = ["Programacion", "Base de datos", "Macroeconomia", "Estadistica", "Contabilidad" ]
    reprobados = registros[(registros < 70)]
    print("ALUMNOS CON MAS DE 2 MATERIAS REPROBADAS")
    alumnos_rep = reprobados.count() >= 2
    print(*alumnos_rep[alumnos_rep].index)
    print(separador)
    archivoTexto2.write("\nALUMNOS CON MAS DE 2 MATERIAS REPROBADAS \n")
    archivoTexto2.write(*alumnos_rep[alumnos_rep].index)
    archivoTexto2.close()
    menu()

menu()