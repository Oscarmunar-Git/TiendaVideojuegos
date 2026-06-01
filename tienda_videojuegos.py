# =====================================
# SISTEMA DE GESTIÓN DE VIDEOJUEGOS
# =====================================

videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },
    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },
    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}

historial_ventas = []


def agregar_videojuego(videojuegos):
    codigo = input("Código: ")

    if codigo in videojuegos:
        print("El código ya existe.")
        return

    nombre = input("Nombre: ")
    plataforma = input("Plataforma: ")

    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    if precio <= 0 or cantidad <= 0:
        print("Precio y cantidad deben ser mayores que cero.")
        return

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Videojuego agregado correctamente.")


def mostrar_inventario(videojuegos):

    if not videojuegos:
        print("No hay videojuegos registrados.")
        return

    print("\n===== INVENTARIO =====")

    for codigo, datos in videojuegos.items():
        print(f"""
Código: {codigo}
Nombre: {datos['nombre']}
Plataforma: {datos['plataforma']}
Precio: ${datos['precio']}
Cantidad: {datos['cantidad']}
--------------------------
""")


def buscar_videojuego(videojuegos):

    codigo = input("Ingrese código: ")

    if codigo in videojuegos:
        juego = videojuegos[codigo]

        print(f"""
Nombre: {juego['nombre']}
Plataforma: {juego['plataforma']}
Precio: ${juego['precio']}
Cantidad: {juego['cantidad']}
""")
    else:
        print("Videojuego no encontrado.")


def actualizar_precio(videojuegos):

    codigo = input("Código del videojuego: ")

    if codigo in videojuegos:
        nuevo_precio = float(input("Nuevo precio: "))
        videojuegos[codigo]["precio"] = nuevo_precio
        print("Precio actualizado.")
    else:
        print("Videojuego no encontrado.")


def registrar_venta(videojuegos):

    codigo = input("Código del videojuego: ")

    if codigo not in videojuegos:
        print("Videojuego no existe.")
        return

    cantidad = int(input("Cantidad a vender: "))

    if cantidad > videojuegos[codigo]["cantidad"]:
        print("Inventario insuficiente.")
        return

    precio = videojuegos[codigo]["precio"]
    total = precio * cantidad

    if total > 500000:
        total *= 0.90

    videojuegos[codigo]["cantidad"] -= cantidad

    historial_ventas.append({
        "codigo": codigo,
        "cantidad": cantidad,
        "total": total
    })

    print("\nFactura")
    print("-------")
    print("Juego:", videojuegos[codigo]["nombre"])
    print("Precio unitario:", precio)
    print("Cantidad:", cantidad)
    print("Total:", total)


def mostrar_estadisticas(videojuegos):

    total_juegos = len(videojuegos)

    valor_inventario = 0

    juego_costoso = max(
        videojuegos,
        key=lambda x: videojuegos[x]["precio"]
    )

    juego_stock = max(
        videojuegos,
        key=lambda x: videojuegos[x]["cantidad"]
    )

    suma_precios = 0

    for datos in videojuegos.values():
        valor_inventario += datos["precio"] * datos["cantidad"]
        suma_precios += datos["precio"]

    promedio = suma_precios / total_juegos

    print("\n===== ESTADÍSTICAS =====")
    print("Total videojuegos:", total_juegos)
    print("Valor inventario:", valor_inventario)
    print("Más costoso:", videojuegos[juego_costoso]["nombre"])
    print("Mayor cantidad:", videojuegos[juego_stock]["nombre"])
    print("Promedio precios:", promedio)


def eliminar_videojuego(videojuegos):

    codigo = input("Código a eliminar: ")

    if codigo in videojuegos:
        del videojuegos[codigo]
        print("Videojuego eliminado.")
    else:
        print("Videojuego no encontrado.")


def menu():

    while True:

        print("""
===== TIENDA DE VIDEOJUEGOS =====
1. Agregar videojuego
2. Mostrar inventario
3. Buscar videojuego por código
4. Actualizar precio
5. Registrar venta
6. Mostrar estadísticas
7. Eliminar videojuego
8. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_videojuego(videojuegos)

        elif opcion == "2":
            mostrar_inventario(videojuegos)

        elif opcion == "3":
            buscar_videojuego(videojuegos)

        elif opcion == "4":
            actualizar_precio(videojuegos)

        elif opcion == "5":
            registrar_venta(videojuegos)

        elif opcion == "6":
            mostrar_estadisticas(videojuegos)

        elif opcion == "7":
            eliminar_videojuego(videojuegos)

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()