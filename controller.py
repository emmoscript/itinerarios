import sqlite3 as sql


def createDB():
    conn = sql.connect("itinerario.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE salidas (
            origen text,
            aeropuerto text,
            fecha date,
            hora time,
            vuelo integer,
            aerolínea text
        )"""
    )
    cursor.execute(
        """CREATE TABLE llegadas (
            destino text,
            aeropuerto text,
            fecha date,
            hora time,
            vuelo integer,
            aerolínea text
        )"""
    )
    cursor.execute(
        """CREATE TABLE mod (
            caso text,
            fecha date,
            hora time,
            vuelo integer,
            aerolínea text
        )"""
    )
    conn.commit()
    conn.close()


def insertSalida(itinerarios_salida):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO salidas (origen, aeropuerto, fecha, hora, vuelo, aerolínea) VALUES (?, ?, ?, ?, ?, ?)"
    for itinerario in itinerarios_salida:
        cursor.execute(instruccion, itinerario)
    conn.commit()
    conn.close()

def insertLlegada(itinerarios_llegada):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO llegadas (destino, aeropuerto, fecha, hora, vuelo, aerolínea) VALUES (?, ?, ?, ?, ?, ?)"
    for itinerario in itinerarios_llegada:
        cursor.execute(instruccion, itinerario)
    conn.commit()
    conn.close()

def insertCaso(itinerarios_caso):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO mod (caso, fecha, hora, vuelo, aerolínea) VALUES (?, ?, ?, ?, ?)"
    for itinerario in itinerarios_caso:
        cursor.execute(instruccion, itinerario)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM llegadas"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def readOrdered(field):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM itinerario ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def searchByVuelo(vuelo):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM salidas WHERE vuelo = ?"
    cursor.execute(instruccion, (vuelo,))
    datos = cursor.fetchall()
    conn.close()
    print(datos)

def searchByOrigen(origen, aerolínea):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM salidas WHERE origen = ? AND aerolínea = ?"
    cursor.execute(instruccion, (origen, aerolínea))
    datos = cursor.fetchall()
    conn.close()
    print(datos)

def searchByVueloLlegadas(vuelo):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM llegadas WHERE vuelo = ?"
    cursor.execute(instruccion, (vuelo,))
    datos = cursor.fetchall()
    conn.close()
    if datos:
        print("Resultados de búsqueda en Llegadas:")
        for row in datos:
            print(row)
    else:
        print("No se encontraron resultados para ese número de vuelo en Llegadas.")

def searchByDestinoLlegadas(destino, aerolinea):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM llegadas WHERE destino = ? AND aerolínea = ?"
    cursor.execute(instruccion, (destino, aerolinea))
    datos = cursor.fetchall()
    conn.close()
    if datos:
        print("Resultados de búsqueda en Llegadas:")
        for row in datos:
            print(row)
    else:
        print("No se encontraron resultados para ese destino y aerolínea en Llegadas.")


def updateFields():
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE salidas SET vuelo=719 WHERE vuelo like '817'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
  
def deleteRow():
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM itinerario WHERE origen='SAN JUAN'"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()
    
def searchByDestinoBidireccional(destino, aerolinea):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    
    instruccion_salidas = f"SELECT * FROM salidas WHERE destino = ? AND aerolínea = ?"
    cursor.execute(instruccion_salidas, (destino, aerolinea))
    datos_salidas = cursor.fetchall()
    
    instruccion_llegadas = f"SELECT * FROM llegadas WHERE origen = ? AND aerolínea = ?"
    cursor.execute(instruccion_llegadas, (destino, aerolinea))
    datos_llegadas = cursor.fetchall()
    
    conn.close()
    
    if datos_salidas or datos_llegadas:
        print("Resultados de búsqueda en Salidas:")
        for row in datos_salidas:
            print(row)
        print("Resultados de búsqueda en Llegadas:")
        for row in datos_llegadas:
            print(row)
    else:
        print("No se encontraron resultados para ese destino y aerolínea en Salidas ni en Llegadas.")

def searchVueloTridimensional(nvuelo):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    
    instruccion_salidas = f"SELECT * FROM salidas WHERE vuelo = ?"
    cursor.execute(instruccion_salidas,(nvuelo,))
    datos_salidas = cursor.fetchall()
    
    instruccion_llegadas = f"SELECT * FROM llegadas WHERE vuelo = ?"
    cursor.execute(instruccion_llegadas,(nvuelo,))
    datos_llegadas = cursor.fetchall()

    instruccion_mod = f"SELECT * FROM mod WHERE vuelo = ?"
    cursor.execute(instruccion_mod,(nvuelo,))
    datos_mod = cursor.fetchall()
    
    conn.close()
    
    if datos_salidas or datos_llegadas or datos_mod:
        print("Resultados de búsqueda en Salidas:")
        for row in datos_salidas:
            print(row)
        print("Resultados de búsqueda en Llegadas:")
        for row in datos_llegadas:
            print(row)
        print("Resultados de búsqueda en Modificaciones:")
        for row in datos_mod:
            print(row)
    else:
        print("No se encontraron resultados para ese destino y aerolínea en Salidas ni en Llegadas.")


if __name__ == "__main__":
    #createDB()
    #createTable()
    #readRows()
    itinerarios_salida = [
        ("SAN JUAN", "SJU", "2023-09-10", "11:34", 97, "JetBlue"),
        ("FORT LAUDERDALE", "FLL", "2023-09-10", "12:36", 2549, "JetBlue"),
        ("NEW YORK", "JFK", "2023-09-10", "13:12", 9, "JetBlue"),
        ("NEWARK", "EWR", "2023-09-10 ", "13:55", 2404, "United Airlines"),
        ("MADRID", "MAD", "2023-09-10", "14:30", 6501, "Iberia"),
        ("NEW YORK", "JFK", "2023-09-10", "14:34", 210, "JetBlue"),
        ("EL SALVADOR", "SAL", "2023-09-10", "15:15", 4451, "Arajet"),
        ("MANAGUA ", "MGA ", "2023-09-10", "16:05", 1813, "SKYhigh"),
        ("PANAMÁ", "PTY", "2023-09-10", "16:13", 128, "Copa Airlines"),
        ("MIAMI", "MIA", "2023-09-10", "16:30", 906, "SKYhigh"),
        ("SAN JUAN", "SJU", "2023-09-10", "16:36", 1637, "JetBlue"),
        ("NEW YORK", "JFK", "2023-09-10", "16:52", 1908, "Delta"),
        ("BOGOTA", "BOG", "2023-09-10", "17:35", 250, "Avianca"),
        ("LIMA", "LIM", "2023-09-10", "20:20", 3663, "Arajet")
    ]
    itinerarios_llegada = [
        ("SAN JUAN", "SJU", "2023-09-10", "12:44", 96, "Frontier Airlines"),
        ("TORTOLA", "EIS", "2023-09-10", "14:05", 411, "National Air Charters"),
        ("PROVIDENCIALES", "PLS", "2023-09-10", "14:25", 234, "interCaribbean Airways"),
        ("NEW YORK", "JFK", "2023-09-10", "14:34", 210, "JetBlue"),
        ("ATLANTA", "ATL", "2023-09-10", "14:43", 1803, "Delta"),
        ("ORLANDO", "MCO", "2023-09-10", "15:02", 1406, "JetBlue"),
        ("FORT LAUDERDALE", "FLL", "2023-09-10", "15:50", 142, "Spirit"),
        ("MADRID", "MAD", "2023-09-10", "16:05", 6500, "Iberia"),
        ("MIAMI", "MIA", "2023-09-10", "16:05", 1154, "American Airlines"),
        ("NEWARK", "EWR", "2023-09-10", "16:30", 2604, "JetBlue"),
        ("NEW YORK", "JFK", "2023-09-10", "17:15", 2510, "JetBlue"),
        ("SAN JUAN", "SJU", "2023-09-10", "17:36", 1638, "JetBlue"),
        ("SAINT VINCENT", "SVD", "2023-09-10", "17:45", 1501, "SKyhigh"),
        ("HOLGUÍN/CUBA", "HOG", "2023-09-10", "18:00", 1906, "Frontier Airlines"),
        ("CAMAGUEY/CUBA", "CMW", "2023-09-10", "18:00", 832, "Frontier Airlines")
    ]
    itinerarios_caso = [
        ("ATRASADO","2023-09-10", "11:34", 97, "JetBlue"),
        ("CANCELADO","2023-09-10", "17:36", 1638, "JetBlue"),
        ("ATRASADO","2023-09-10", "18:00", 832, "Frontier Airlines"),
          ("ATRASADO","2023-09-10", "12:44", 96, "Frontier Airlines"),
        ("CANCELADO","2023-09-10", "14:05", 411, "National Air Charters")
    ]
    itinerarios_caso_tridiagonal = [
        ["ATRASADO","2023-09-10", "","", "                                    "],
        ["CANCELADO","2023-09-10", "17:36","", "                             "],
        ["          ","2023-09-10", "18:00", 832, "                         "],
          ["            ","             ", "12:44", 96, "Frontier Airlines       "],
        ["             ","           ", "         ", 411, "National Air Charters"],    
    ]
    itinerarios_caso_poco_denso = [
        ("ATRASADO","2023-09-10", "         ", 97, "JetBlue"),
        ("         ","2023-09-10", "         ", "         ", "JetBlue"),
        ("         ","         ", "18:00", "         ", "         "),
          ("      ","         ", "         ", "         ", "Frontier Airlines"),
        ("CANCELADO","2023-09-10", "14:05", 411, "         ")
    ]
    
    #Código Actividad 2.1
    a = 235.5
    b = 545.6
    c = 323.9
    itinerarios_caso_simetrica = [
        ("132.1", a, b),
        (a, "255.99", c),
        (b, c, "654.8"),
    ]
    itinerarios_caso_antisimetrica = [
        ("132.1", a, b),
        (-a, "255.99", c),
        (-b, -c, "654.8"),
    ]
    #Asientos donde 0 = no ocupado y 1 = ocupado
    itinerarios_caso_binario = [
        "(A, B, C, D, E, F)",
        (0,1,1,1,0,1),
        (0,0,0,1,1,0),
        (1,1,1,1,0,1),
        (0,0,0,0,0,1),
        (1,1,1,0,0,1),
        (0,0,0,0,1,0)
    ]
    #insertSalida(itinerarios_salida)
    #insertLlegada(itinerarios_llegada)
    #readOrdered("vuelo")
    #insertCaso(itinerarios_caso)
    #search()
    #updateFields()
    #deleteRow()
    #searchByVuelo(128)
    #searchByOrigen("NEW YORK","JetBlue")
    while True:
        print("Menú de Opciones:")
        print("1. Buscar por número de vuelo en Salidas")
        print("2. Imprimir matriz tridiagonal")
        print("3. Imprimir matriz de poca densidad")
        print("4. Buscar en tres dimensiones")
        print("5. Buscar por destino y aerolínea en Salidas y Llegadas (Bidireccional)")
        print("6. Imprimir matriz simétrica")
        print("7. Imprimir matriz anti-simétrica")
        print("8. Imprimir matriz binaria")
        print("9. Salir")
        
        opcion = input("Ingrese el número de la opción que desea: ")
        
        if opcion == "1":
            vuelo = input("Ingrese el número de vuelo que desea buscar en Salidas: ")
            searchByVuelo(vuelo)
        
        elif opcion == "2":
            print("\nAqui hay una representacion de una matriz tridiagonal\n")
            for line in itinerarios_caso_tridiagonal:
                print(f'{line}\n')
            
        elif opcion == "3":
            print("\nAqui hay una representacion de una matriz de poca densidad\n")
            for line in itinerarios_caso_poco_denso:
                print(f'{line}\n')
        
        elif opcion == "4":
            numero = input("Ingrese el numero de vuelo que quiere buscar en las tres matrices: ")
            searchVueloTridimensional(numero)
        
        elif opcion == "5":
            destino = input("Ingrese el destino que desea buscar en Salidas y Llegadas: ")
            aerolinea = input("Ingrese la aerolínea que desea buscar en Salidas y Llegadas: ")
            searchByDestinoBidireccional(destino, aerolinea)
        
        elif opcion == "6":
            for line in itinerarios_caso_simetrica:
                print(f'\n{line}')    
            print('\n')
        
        elif opcion == "7":
            for line in itinerarios_caso_antisimetrica:
                print(f'\n{line}')    
            print('\n') 

        
        elif opcion == "8":
            for line in itinerarios_caso_binario:
                print(f'\n{line}')    
            print('\n') 
        
        elif opcion == "9":
            print()
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
