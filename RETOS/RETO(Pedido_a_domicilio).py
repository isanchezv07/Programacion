# Inicializa la variable para acumular el costo total del pedido
pedido_total = 0

print("Bienvenido al sistema de pedido a domicilio.")
print("--------------------")
print("1. Pizza - $10")
print("2. Hamburguesa - $8")
print("3. Ensalada - $7")
print("4. Ver total del pedido")
print("0. Finalizar pedido")
print("--------------------")

while True:
    # Solicita al usuario que ingrese el número de la opción deseada
    opcion = input("Introduce el número de la opción que deseas: ")

    # Verifica la opción seleccionada
    match opcion:
        case '1':
            pedido_total += 10
            print("Añadiste Pizza a tu pedido. Total actual: $", pedido_total)
        case '2':
            pedido_total += 8
            print("Añadiste Hamburguesa a tu pedido. Total actual: $", pedido_total)
        case '3':
            pedido_total += 7
            print("Añadiste Ensalada a tu pedido. Total actual: $", pedido_total)
        case '4':
            print("El total de su pedido hasta ahora es: $", pedido_total)
            continue  # Permite al usuario seguir sin salir del bucle
        case '0':
            print("El total de su pedido es: $", pedido_total)
            print("Gracias por su pedido. ¡Buen provecho!")
            break  # Termina el bucle
        case _:
            print("Opción no válida. Por favor, intenta nuevamente.")
            continue  # Permite al usuario seguir sin salir del bucle

    # Pregunta al usuario si desea continuar añadiendo productos
    if opcion != '0':
            continuar = input("¿Deseas seguir añadiendo productos? (sí/no): ").strip().lower()
        if continuar == 'no':
            print("El total de su pedido es: $", pedido_total)
            print("Gracias por su pedido. ¡Buen provecho!")
            break  # Termina el bucle