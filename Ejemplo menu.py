juegos = [['Catan', 4], ['Dixit', 2], ['Virus', 6], ['Carcassonne', 3]]
opcion = ""

while opcion != "g":
    print("a) Añadir un nuevo juego ")
    print("b) Mostrar la lista de juegos ")
    print("c) Mostrar los juegos ordenados alfabéticamente, de la Z a la A ")
    print("d) Mostrar los juegos ordenados por número de unidades (de menor a mayor) ")
    print("e) Eliminar un juego ")
    print("f) Aplicar mantenimiento ")
    print("g) Prestamo de juegos ")
    print("h) Salir ")
    opcion = input("Elige una opcion ")
    if opcion == "a":
        nom = input("Dime el nombre del juego que quieres añadir ")
        uni = int(input("Dime las unidades del juego que tienes "))
        juegos.append([nom, uni])
    if opcion == "b":
        print(juegos)
    if opcion == "c":
        ordenado_juegos = sorted(juegos, key=lambda juegos: juegos[0], reverse=True)
        print(ordenado_juegos)
    if opcion == "d":
        ordenado_cantidad = sorted(juegos, key=lambda juegos: juegos[1])
        print(ordenado_cantidad)
    if opcion == "e":
        eliminar = input("Dime a quien quieres eliminar ")
        juegos_eliminar = []
        for i in juegos:
            if i[0] == eliminar:
                juegos_eliminar.append(i)

        for a in juegos_eliminar:
            juegos.remove(a)
            print(f"Se ha eliminado a {i}")

    if opcion == "f":
        for i in juegos:
            if i[1] < 3:
                i[1] += 2
        print(juegos)
    if opcion == "g":
        encontrado = False
        eleccion = input("Dime que juego te quieres que te deje ")
        for i in juegos:
            if i[0] == eleccion:
                encontrado = True
            print("El juego que buscas lo tenemos ")
            if i[0] != eleccion:
                print("El juego que buscas no lo tenemos ")
            if i[1] > 0:
                if i[1] == juegos:
                    juegos[1] -= 1
                    print(f"Te vamos a prestar el juego {eleccion} ")
                if i[1] != juegos:
                    print("El juego que buscas no lo tenemos en stock ")
    if opcion == "h":
        break