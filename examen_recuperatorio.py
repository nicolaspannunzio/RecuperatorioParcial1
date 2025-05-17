# Tecnicatura en Programación a Distancia - UTN
# Examen recuperatorio - Programación I
# Alumno: Nicolás A. Pannunzio

###########################################################################################
###########################################################################################


# Lista de productos
productos = []
# Lista de cantidades 
cantidades = []



# Menú principal del programa
def menu_principal():
    print("\n===== GESTOR DE STOCK DE PRODUCTOS=====")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")
    return input("Seleccione una opción: ")



while True:
    opcion = menu_principal()
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad en stock: "))
        productos.append(producto)
        cantidades.append(cantidad)
        print("Producto agregado con éxito")
        

    elif opcion == "2":
        print("Productos agotados: ")
        for i in range(len(productos)):
            if cantidades[i] == 0:
                print(f"Producto: {productos[i]}, Cantidad: {cantidades[i]}")
            else:
                print("No hay productos agotados")
        

    elif opcion == "3":
        print("\n--- ACTUALIZAR STOCK ---")
        produc = input("Ingrese el nombre del producto: ")

        existe = False
        for i in range(len(productos)):
            if productos [i] == produc:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {produc}: "))
                cantidades[i] = nueva_cantidad
                print(f"Stock de {produc} actualizado a {nueva_cantidad}")
                existe = True
                break

        if not existe:         
            print(f"Producto '{produc}' no encontrado")
        

    elif opcion == "4":
        print("\n--- LISTA DE PRODUCTOS ---")
        for i in range(len(productos)):
            print(f"{productos[i]}: {cantidades[i]} unidades")


    elif opcion == "5":
        print("¡Gracias por usar el sistema!")
        break
        

    else:
        print("Opción incorrecta. Intentelo de nuevo.")


###########################################################################################
###########################################################################################