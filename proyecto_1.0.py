import pickle

###############################################################################################################################################
#Main Object: "empleados"
class empleados:

    def __init__(self, nombre, cargo, salario, antiguedad):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.antiguedad=antiguedad
        try:
             with open("EMPLEADOS.pkl", 'rb') as f:
                 EMPLEADOS = pickle.load(f)
        except FileNotFoundError:
            EMPLEADOS = []
        self.id=len(EMPLEADOS)+1

    def __str__(self):
        return (f"""                          
║\t■      Nombre: {self.nombre}                
║\t■       Cargo: {self.cargo}                 
║\t■     Salario: {self.salario}               
║\t■  Antigüedad: {self.antiguedad}
║                                         
╚════════════════════╦═════════════════════""")

###############################################################################################################################################
#Función "Crear Empleado":
def crearEmpleado():
        
# #Validación de pre-existencia de empleado:
        # for i, empleado in enumerate(EMPLEADOS):
        #         if (EMPLEADOS[i].nombre==nombre):
        #             print(f"El empleado {nombre} ya existe en el registro.\n")
        #             main() ############Poner algo que cierre el programa al terminar el main() aca BUG ##################
        ##########################################

    nombre=input(""" 

    ╔═══════════════════════════════╗
╔═══╣ Nombre completo del empleado: ║
║   ╚═══════════════════════════════╝
║     » """)
    cargo=input("""║
║  ╔══════════════════╗
╠══╣ Cargo que ocupa: ║
║  ╚══════════════════╝
║     » """)
    salario=input("""║
║   ╔═══════════╗
╠═══╣ Salario:  ║
║   ╚═══════════╝
║     » """)
    antiguedad=input("""║ 
║   ╔════════════════════════════╗
╠═══╣ Antigüedad en la empresa:  ║
║   ╚════════════════════════════╝
║     » """)
    
    empleado= empleados(nombre,cargo,salario,antiguedad)

    try:
        with open("EMPLEADOS.pkl", 'rb') as f:
            EMPLEADOS = pickle.load(f)
    except FileNotFoundError:
        EMPLEADOS = []
    with open('EMPLEADOS.pkl', 'wb') as f:
        EMPLEADOS.append(empleado)
        pickle.dump(EMPLEADOS, f)

    print("""║
║           ╔══════════════════════════════════════════╗
╚═══════════╣  » ¡Empleado registrado exitosamente! «  ║
            ╚══════════════════════════════════════════╝
""")

###############################################################################################################################################
#Función "Ver Datos de Empleado":
def mostrarDatos():
            
    Nombre= input(""" 
           ╔════════════════════════════════════════════════════════════════════╗
═══════════╣  » Por favor ingrese el nombre del empleado que desea examinar:    ║
           ║      (ingrese 'TODOS' para ver la totalidad de la nomina)          ║
           ╚════════════════════════════════════════════════════════════════════╝
             » """)
    
    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            lista=pickle.load(f)

        if len(lista)>0:
            if (Nombre=="TODOS"):
                with open("EMPLEADOS.pkl", "rb") as f:
                    lista=pickle.load(f)
                    for i in (lista):
                        id=i.id
                        print(f"""                ╔════╩═══╗
╔═══════════════╣ ID: {id}  ╠═════════════════
║               ╚════════╝""",i)
            else:
                for i, empleado in enumerate(lista):
                    id=empleado.id
                    if (empleado.nombre==Nombre):
                        print(f"""                 ╔═══════════╗
╔════════════════╣   ID: {id}   ╠════════════════
║                ╚═══════════╝
║ \t   ■      Nombre: {empleado.nombre}         
║ \t   ■       Cargo: {empleado.cargo}          
║ \t   ■     Salario: {empleado.salario}        
║ \t   ■  Antigüedad: {empleado.antiguedad}
║
╚═════════════════════════════════════════════

        """)
                        break
                    else:
                        if (i==len(lista)-1):
                            print("""
            ╔════════════════════════════════════════════════════════════╗
    ═══════════╣    » El nombre es incorrecto, o el empleado no existe.     ║
            ║      Por favor chequee los datos y vuelva a intentarlo.    ║
            ╚════════════════════════════════════════════════════════════╝
            """)
            
        else:
            print("No se encontraron empleados. Revise su base de datos de forma externa o consulte a servicio técnico.")
    except FileNotFoundError:
        print("No se encontraron empleados. Revise su base de datos de forma externa o consulte a servicio técnico.")

###############################################################################################################################################
# Función "Modificar Datos de Empleado":

def modificarDatos():

    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            EMPLEADOS=pickle.load(f)
        
        Nombre= input("""  
            ╔═══════════════════════════════════════════════════════════╗
╔═══════════╣  » Por favor ingrese el nombre del empleado a modificar:  ║
║           ╚═══════════════════════════════════════════════════════════╝
║            » """)
        dato= input("""║ 
║           ╔═════════════════════════════════════════════╗
╠═══════════╣  » Por favor ingrese el dato a modificar:   ║
║           ╚═════════════════════════════════════════════╝
║            » """)
        nuevoValor= input(f"""║  
║           ╔════════════════════════════════════════════════════════
╠═══════════╣  » Por favor ingrese el nuevo valor de {dato}.            
║           ╚════════════════════════════════════════════════════════
║            » """)

        for i, empleado in enumerate(EMPLEADOS):
            if (EMPLEADOS[i].nombre==Nombre):
                with open("EMPLEADOS.pkl", "wb") as f:
                    setattr(EMPLEADOS[i], dato, nuevoValor)
                    print(f"""║ 
    ║           ╔═════════════════════════════════════════════════════════════════════
    ╚═══════════╣  » Para el empleado/a: {Nombre} el {dato} ha sido modificado a:                                
                ║     {getattr(EMPLEADOS[i], dato)}.                                                              
                ╚═════════════════════════════════════════════════════════════════════
                """)
                    pickle.dump(EMPLEADOS, f)
                break
            else:
                if (i==len(EMPLEADOS)-1):
                    print("""║ 
║           ╔═════════════════════════════════════════════════════════════════════════════════════════════════════════╗
╚═══════════╣  » El nombre es incorrecto, o el empleado no existe. Por favor chequee los datos y vuelva a intentarlo. ║                                                             ║
            ╚═════════════════════════════════════════════════════════════════════════════════════════════════════════╝
            » """)
    except FileNotFoundError:
        print("""No se encontraron empleados. Verifique la base de datos o contacte con soporte técnico.
    """)

###############################################################################################################################################
#Función "Eliminar Empleado":
def eliminarEmpleado():

    try:
        with open("EMPLEADOS.pkl", "rb") as f:
            EMPLEADOS=pickle.load(f)

        if len(EMPLEADOS)>0:
            
            Nombre= input("» Por favor ingrese el nombre del empleado que desea eliminar del registro: \n")

            with open("EMPLEADOS.pkl", "wb") as f:

                for i, empleado in enumerate(EMPLEADOS):
                    if (EMPLEADOS[i].nombre==Nombre):
                        del EMPLEADOS[i]
                        print(f"El empleado: {Nombre} ha sido eliminado del registro. \n")
                        pickle.dump(EMPLEADOS, f)
                        break
                    if (i==len(EMPLEADOS)-1):
                        print("El nombre es incorrecto, o el empleado no existe. Por favor chequee los datos y vuelva a intentarlo. \n")
        else:
            print("No se encontraron empleados. Revise su base de datos de forma externa o consulte a servicio técnico.")

    except FileNotFoundError:
        print("No se encontraron empleados. Revise su base de datos de forma externa o consulte a servicio técnico.")

###############################################################################################################################################
#Función Menú Principal:
def opciones():
    option=input("""
                 ╔═══════════════════════════════════════════════════════════════╗
╔════════════════╣ Por favor, ingrese el número de la acción que desea realizar: ╠═══════════════╗
║                ╚═══════════════════════════════════════════════════════════════╝               ║
║ \t\t   ■      1»  Agregar un empleado al registro.                                   ║
║ \t\t   ■      2»  Mostrar los datos de un empleado.                                  ║
║ \t\t   ■      3»  Modificar los datos de un empleado.                                ║    
║ \t\t   ■      4»  Eliminar un empleado del registro.                                 ║
║ \t\t   ■      5»  Cerrar el programa.                                                ║
║                                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════════════════════╝
      » """)

    if (option=="1"):
        crearEmpleado()
    elif (option=="2"):
        mostrarDatos()
    elif (option=="3"):
        modificarDatos()
    elif (option=="4"):
        eliminarEmpleado()
    elif (option=="5"):
        keepRunning()
    else:
        print("La opción seleccionada no es válida.\n")
        main()

#Salir del programa:
def keepRunning():

    choice=""
    choice=input("""
    \t\t        ╔═════════════════════════════════════════════════╗
    \t\t        ║ » ¿Desea realizar alguna otra operación? (S/N)  ║                                             
    \t\t        ╚═════════════════════════════════════════════════╝
     » """)
    if (choice!="S" and choice!="N"):
        print("» No es una opción válida. Por favor ingrese: (S/N) \n")
        keepRunning()
    return choice

#Definición de la Ejecución principal del programa
def main():

    while True:

        opciones()

        keepRunning()

        if (keepRunning()=="N"):
            break

#Ejecución de la Pantalla del Usuario:
main()