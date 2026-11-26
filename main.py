
      productos = []

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: el texto no puede quedar vacío.")

def pedir_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje).strip())
            if valor > 0:
                return valor
            print("Error: el número debe ser mayor a 0.")
        except ValueError:
            print("Error: ingresá un número decimal válido.")

def pedir_int_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor >= 0:
                return valor
            print("Error: el número debe ser mayor o igual a 0.")
        except ValueError:
            print("Error: ingresá un número entero válido.")

def agregar_producto(productos):
    print("\n--- AGREGAR PRODUCTO ---")
    nombre = pedir_texto("Nombre del producto: ")
    for p in productos:
        if p["nombre"].lower() == nombre.lower():
            print("Error: ya existe un producto con ese nombre.")
            return
    precio = pedir_float_positivo("Precio unitario ($): ")
    stock = pedir_int_no_negativo("Stock inicial: ")
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    })
    print(f"Producto '{nombre}' guardado correctamente.")

def mostrar_menu():
    print("\n--- GESTOR DE STOCK ALMACÉN SLP ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Modificar precio o stock")
    print("5. Eliminar producto")
    print("6. Ver alertas de stock bajo y valor total")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-7): ").strip()
        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        elif opcion in ["2", "3", "4", "5", "6"]:
            print(f"Opción {opcion} seleccionada (en desarrollo).")
        else:
            print("Opción inválida. Ingresá un número del 1 al 7.")

if _name_ == "_main_":
    main()
