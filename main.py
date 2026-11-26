productos = []

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
        if opcion == "7":
            print("Saliendo del sistema...")
            break
        elif opcion in ["1", "2", "3", "4", "5", "6"]:
            print(f"Opción {opcion} seleccionada (en desarrollo).")
        else:
            print("Opción inválida. Ingresá un número del 1 al 7.")

if _name_ == "_main_":
    main()
