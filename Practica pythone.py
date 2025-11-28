catalogo = [
 ["Super Mario Bros", "plataformas", "Nintendo", 5, 1985],
 ["Sonic the Hedgehog", "plataformas", "Sega", 4, 1991],
 ["The Legend of Zelda", "aventura", "Nintendo", 5, 1986],
 ["Doom", "shooter", "PC", 5, 1993],
 ["Final Fantasy VII", "rol", "PlayStation", 5, 1997],
 ["Pac-Man", "arcade", "Arcade", 4, 1980]
]
opcion = ""
sublista = ""


while opcion != "d":
    print("a) Mostrar estadísticas del catálogo")
    print("b) Filtrar juegos por año")
    print("c) Añadir juego al catálogo")
    print("d) Salir")
    opcion = input("Dime la opcion que te gustaria elegir ")

    if opcion == "a":
        print("1. Mostrar la media de valoraciones del catálogo ")
        print("2. Ver el juego más antiguo y el más reciente. ")
        print("3. Salir. ")
        sublista = input("Dime que opcion quieres elegir ")

        if sublista == "1":
            media_catalogo = sum(i[3] for i in catalogo) / len(catalogo)
            print(media_catalogo)

        if sublista == "2":
            catalogo.sort(key=lambda catalogo:catalogo[4])
            print(f"El juego mas antiguo es {catalogo[0]} y el juego mas reciente es {catalogo[-1]}")
    
    if opcion == "b":
        filtro = int(input("Dime de que año quieres que sea el juego "))
        años = False
        for i in catalogo:
            if filtro == i[4]:
                años = True
                print(i)
        else:
            print(f"No hay ningun juego en el año {i}")

    if opcion == "d":
        print("Muchas gracias por utilizar nuestro programa. ")