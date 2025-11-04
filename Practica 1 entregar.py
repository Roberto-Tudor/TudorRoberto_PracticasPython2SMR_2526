import random

usuarios = []

while True:
    nombre = input("Introduce el nombre del usuario: ")
    contraseña = input("Introduce la contraseña del usuario: ")
    usuarios.append([nombre, contraseña])
    seguir = input("¿Quieres añadir un nuevo usuario? (si/no): ").lower()
    if seguir != "si":
        break


contraseñas_inseguras = ["1234", "password", "qwerty", "abc123", "hola"]


usuarios_vulnerados = [] 
usuarios_resistentes = [] 


seguir_atacando = True

while seguir_atacando:
    
    usuario = random.choice(usuarios)
    nombre_usuario = usuario[0]
    contraseña_usuario = usuario[1]

    
    for insegura in contraseñas_inseguras:
        if contraseña_usuario.lower() == insegura.lower():
            print(f"El usuario {nombre_usuario} fue vulnerado. Contraseña débil.")
            usuarios_vulnerados.append(nombre_usuario)
            break
    else:
        
        print(f"El usuario {nombre_usuario} resistió el ataque.")
        usuarios_resistentes.append(nombre_usuario)

    
    respuesta = input("¿Quieres hacer otro intento de ataque? (si/no): ").lower()
    if respuesta != "si":
        seguir_atacando = False


print("Resumen de vulnerabilidades")
print("Usuarios vulnerados:")
for u in usuarios_vulnerados:
    print(f"{u}")

print("Usuarios que resistieron el ataque:")
for u in usuarios_resistentes:
    print(f"{u}")