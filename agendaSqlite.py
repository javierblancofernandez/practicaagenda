
import sqlite3 as lite
import sys

# Conexion a la BBDD Sqlite 
def conexion():
    conexion = lite.connect('agenda.sqlite')
    return conexion
# Menu del sistema   
def menu():
    print("Programa practica Agenda 1roDAM IMF Madrid")
    print("Escoge una de las opciones :")
    print("1.Listar")
    print("2.Buscar")
    print("3.Insertar")
    print("4.Actualizar")
    print("5.Borrar")
    print("6.Salir")
    # escoge una opcion input
    opcion = int(input("Opcion seleccionada :"))
    #ponemos menu para que sea bucle
    if opcion == 1:
        print("estas en listar")
        listar()
    elif opcion == 2:
        print("buscar")
        criterio = input("Indica a quien buscas :")
        buscar(criterio)
    elif opcion == 3:
        print("estas en insertar")
        nombre = input("Introduce el nombre:")
        apellidos = input("Introduce el apellidos: ")
        telefono = input("Introduce el telefono: ")
        email = input("Introduce el email: ")
        insertar_agenda(nombre,apellidos,telefono,email)
    elif opcion == 4:
        print("actualizar")
        id = int(input("dime el id del registro que quieres actualizar :"))
        nombre = input("nombre :")
        apellidos = input("apellidos :")
        telefono = input("telefono :")
        email = input("email :")
        actualizar(id,nombre,apellidos,telefono,email)
    elif opcion == 5:
        print("borrar")
        id = input("dime el id del registro que quieres borrar :")
        borrar(id)
    else:
        print("adios")
        salir()
    #concurrencia
    menu()
#Listar los registros de la agenda
def listar():
    try:
        connect = conexion()
        cursor = connect.cursor()
        agendas = cursor.execute("SELECT * FROM agenda")
        datos = agendas.fetchall()
        if datos:
            print("Lista de películas:")
            for agenda in datos:
                print(f"ID: {agenda[0]}, nombre: {agenda[1]}, apellido: {agenda[2]}, telefono: {agenda[3]}, email: {agenda[4]}")
        else:
            print("No hay películas en la base de datos.")

        cursor.close()
        connect.close()
    except lite.Error as e:
        print("Ocurrió un error al insertar el registro:", e)
#Buscar en los registros de la agenda por criterio
def buscar(criterio):
    try:
        # Establecer la conexión con la base de datos
        connect = conexion()
        # Crear un cursor para ejecutar las consultas
        cursor = connect.cursor()
        agendas = cursor.execute("SELECT * FROM agenda")
        for agenda in agendas: 
            if criterio in agenda:
               print(f"ID: {agenda[0]}, nombre: {agenda[1]}, apellido: {agenda[2]}, telefono: {agenda[3]}, email: {agenda[4]}") 
        cursor.close()
        connect.close()
    except lite.Error as e:
        print("Ocurrió un error al insertar el registro:", e)
#insertar un registro en la agenda
def insertar_agenda(nombre,apellidos,telefono,email):
    try:
        # Establecer la conexión con la base de datos
        connect = conexion()
        # Crear un cursor para ejecutar las consultas
        cursor = connect.cursor()
        # Definir la consulta SQL para insertar el registro
        ##sql = ("INSERT INTO peliculas (genero, titulo, año) VALUES (?, ?, ?)", (genero, titulo, año))"INSERT INTO peliculas (titulo, genero, anio) VALUES ('"+titulo+"', '"+genero+"', '"+anio+"')"
        # Ejecutar la consulta con los valores del registro
        cursor.execute("INSERT INTO agenda (nombre, apellidos, telefono,email) VALUES (?, ?, ?, ?)", (nombre, apellidos, telefono, email))
        # Guardar los cambios en la base de datos
        connect.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        connect.close()
        # Mostrar un mensaje de éxito
        print("registro insertado correctamente")
    except lite.Error as e:
        print("Ocurrió un error al insertar el registro:", e)
#Actualizar un registro de la agenda
def actualizar(id,nombre,apellidos,telefono,email):
    try:
        # Establecer la conexión con la base de datos
        connect = conexion()
        # Crear un cursor para ejecutar las consultas
        cursor = connect.cursor()
        agendas = cursor.execute("SELECT * FROM agenda")
        datos = agendas.fetchall()
        for agenda in datos:
            print("id",agenda[0])
            if agenda[0] == id:
                cursor.execute("UPDATE agenda SET nombre=?, apellidos=?,telefono=?, email=? WHERE id=?",(nombre,apellidos,telefono,email,id))
        connect.commit()
        cursor.close()
        connect.close()
    except lite.Error as e:
        print("Ocurrió un error al insertar el registro:", e)
#Borrar un registro de la agenda según el id
def borrar(id):
        try:
            # Establecer la conexión con la base de datos
            connect = conexion()
            # Crear un cursor para ejecutar las consultas
            cursor = connect.cursor()
            agendas = cursor.execute("SELECT * FROM agenda")
            datos = agendas.fetchall()

            for agenda in datos:
                print("id",agenda[0])
                if str(agenda[0]) == id:
                    print("el registro :")
                    print(f"ID: {agenda[0]}, nombre: {agenda[1]}, apellido: {agenda[2]}, telefono: {agenda[3]}, email: {agenda[4]}")
                    print("va a ser borrado")
                    respuesta = input("¿quieres borrarlo? SI/NO")
                    if(respuesta.lower() =='si'):
                        print("el resgistro va a ser borrado")
                        cursor.execute("DELETE FROM agenda WHERE id=?",(id))
                        print("resgistro borrado")
            connect.commit()
            cursor.close()
            connect.close()
        except lite.Error as e:
            print("Ocurrió un error al insertar el registro:", e)
)
#Salir del sistema
def salir():
    sys.exit()

menu()

    
    
    
