# Prueba Final semestre 1
productos = {
    "8475HD": ["HP", 15.6, "32gb", "SSD", "4T", "Intel Core i9", "Nvidia GTX Titan Black"],
    "2175HD": ["Acer", 14, "4gb", "HDD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16gb", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"]
}

stock = {
    "8475HD": [5000000, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1]
}

while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock por marca")
    print("2. Búsqueda por precio")
    print("3. Eliminar producto")
    print("4. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print(" Por favor ingrese un número válido.")
        continue

    if opcion == 1:
        marca = input("Ingrese la marca a consultar: ").strip().capitalize()
        encontrados = False
        for modelo, detalles in productos.items():
            if detalles[0].lower() == marca.lower():
                print(f"Modelo: {modelo}, Precio: ${stock[modelo][0]}, Unidades: {stock[modelo][1]}")
                encontrados = True
        if not encontrados:
            print(" Marca no encontrada.")
        continue

    elif opcion == 2:
        try:
            precio_min = int(input("Ingrese el precio mínimo: "))
            precio_max = int(input("Ingrese el precio máximo: "))
        except ValueError:
            print(" Ingrese valores numéricos válidos.")
            continue

        encontrados = False
        for modelo, datos in stock.items():
            precio = datos[0]
            if precio_min <= precio <= precio_max:
                print(f"Modelo: {modelo}, Marca: {productos[modelo][0]}, Precio: ${precio}, Unidades: {datos[1]}")
                encontrados = True
        if not encontrados:
            print(" No se encontraron productos en ese rango de precio.")
        continue

    elif opcion == 3:
        modelo_eliminar = input("Ingrese el modelo a eliminar: ").strip()
        if modelo_eliminar in productos:
            del productos[modelo_eliminar]
            del stock[modelo_eliminar]
            print(f" Producto '{modelo_eliminar}' eliminado correctamente.")
        else:
            print(" Modelo no encontrado.")
        continue

    elif opcion == 4:
        print(" Programa finalizado.")
        break

    else:
        print(" Ingrese una opción válida.")
        continue
