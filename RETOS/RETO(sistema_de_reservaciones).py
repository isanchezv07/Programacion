# Lista de reservaciones con tuplas (Nombre del cliente, Cantidad de personas)
reservaciones = [
    ("Mario Gonzalez", 4),
    ("Ana Lopez", 2),
    ("Carlos Ramirez", 6),
    ("Elena Torres", 3),
    ("Jorge Perez", 5)
]

# Eliminar una reservación
reservacion_a_eliminar = ("Carlos Ramirez", 6)
if reservacion_a_eliminar in reservaciones:
    reservaciones.remove(reservacion_a_eliminar)
    print(f"🗑️ Reservación eliminada: {reservacion_a_eliminar[0]}")
else:
    print(f"⚠️ No se encontró la reservación de {reservacion_a_eliminar[0]}.")

# Recorrer e imprimir las reservaciones
for nombre, cantidad in reservaciones:
    print(f"✉️ Reservación: {nombre}, Para: {cantidad} personas.")

# Desafío adicional: Función para actualizar una reservación
def actualizar_reservacion(nombre, nueva_cantidad):
    for i, (cliente, _) in enumerate(reservaciones):
        if cliente == nombre:
            reservaciones[i] = (nombre, nueva_cantidad)
            print(f"🔄 Reservación actualizada: {nombre}, Nueva cantidad: {nueva_cantidad}")
            return
    print(f"⚠️ No se encontró la reservación de {nombre}.")

# Prueba de actualización
actualizar_reservacion("Ana Lopez", 4)