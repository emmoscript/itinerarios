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
            destino varchar,
            aeropuerto character,
            fecha date,
            hora time,
            vuelo integer,
            aerolínea varchar
        )"""
    )
    cursor.execute(
        """CREATE TABLE llegadas (
            origen varchar,
            aeropuerto character,
            fecha date,
            hora time,
            vuelo integer,
            aerolínea varchar
        )"""
    )
    conn.commit()
    conn.close()

def insertSalida(itinerarios_salida):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO salidas (destino, aeropuerto, fecha, hora, vuelo, aerolínea) VALUES (?, ?, ?, ?, ?, ?)"
    for itinerario in itinerarios_salida:
        cursor.execute(instruccion, itinerario)
    conn.commit()
    conn.close()

def insertLlegada(itinerarios_llegada):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO llegadas (origen, aeropuerto, fecha, hora, vuelo, aerolínea) VALUES (?, ?, ?, ?, ?, ?)"
    for itinerario in itinerarios_llegada:
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

def searchByOrigen(destino, aerolinea):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM salidas WHERE destino = ? AND aerolínea = ?"
    cursor.execute(instruccion, (destino, aerolinea))
    datos = cursor.fetchall()
    conn.close()
    if datos:
        print("Resultados de búsqueda en Salidas:")
        for row in datos:
            print(row)
    else:
        print("No se encontraron resultados para ese destino y aerolínea en Salidas.")

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

def searchByDestinoLlegadas(origen, aerolinea):
    conn = sql.connect("itinerario.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM llegadas WHERE origen = ? AND aerolínea = ?"
    cursor.execute(instruccion, (origen, aerolinea))
    datos = cursor.fetchall()
    conn.close()
    if datos:
        print("Resultados de búsqueda en Llegadas:")
        for row in datos:
            print(row)
    else:
        print("No se encontraron resultados para ese origen y aerolínea en Llegadas.")

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
    instruccion = f"DELETE FROM itinerario WHERE destino='SAN JUAN'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

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
    #insertSalida(itinerarios_salida)
    #insertLlegada(itinerarios_llegada)
    #readOrdered("vuelo")
    #search()
    #updateFields()
    #deleteRow()
    #searchByVuelo(128)
    #searchByOrigen("NEW YORK","JetBlue")
    while True:
        print("Menú de Opciones:")
        print("1. Buscar por número de vuelo en Salidas")
        print("2. Buscar por origen y aerolínea en Salidas")
        print("3. Buscar por número de vuelo en Llegadas")
        print("4. Buscar por destino y aerolínea en Llegadas")
        print("5. Salir")
        
        opcion = input("Ingrese el número de la opción que desea: ")
        
        if opcion == "1":
            vuelo = input("Ingrese el número de vuelo que desea buscar en Salidas: ")
            searchByVuelo(vuelo)
        
        elif opcion == "2":
            destino = input("Ingrese el destino que desea buscar en Salidas: ")
            aerolinea = input("Ingrese la aerolínea que desea buscar en Salidas: ")
            searchByOrigen(destino, aerolinea)
        
        elif opcion == "3":
            vuelo = input("Ingrese el número de vuelo que desea buscar en Llegadas: ")
            # Llama a una función de búsqueda en Llegadas
            searchByVueloLlegadas(vuelo)
        
        elif opcion == "4":
            origen = input("Ingrese el origen que desea buscar en Llegadas: ")
            aerolinea = input("Ingrese la aerolínea que desea buscar en Llegadas: ")
            # Llama a una función de búsqueda en Llegadas
            searchByDestinoLlegadas(origen, aerolinea)
        
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
