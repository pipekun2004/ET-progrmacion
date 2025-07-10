# Prueba Final semestre 1
#productos={modelos:[maarca,pantalla,ram,dico,gbdedd, procesador, video]}
productos={"8475HD":["HP",15.6,"32gb","SSD","4T","Intel Core i9","Nvidia GTX Titan Black"],
           "2175HD":["Acer",14,"4gb","HDD","512GB","Intel Core i5","Nvidia GTX1050"],
           "JjfFHD":["Asus",14,"16gb","SSD","256GB","Intel Core i7","Nvidia RTX2080Ti"]}
stock={"8475HD":[5000000,10],
       "2175HD":[327990,4],
       "JjfFHD":[424990,1]}


while True:
    print("***MENU PRINCIPAL***")
    print("1. Stock marca")
    print("2. Busqueda por precio")
    print("3. Eliminar producto")
    print("4. Salir")
    opcion = int(input("selecione una opcion: "))
    if opcion == 1:
        marca=input("ingrese marca a consultar: ")
        if marca == "HP":
            print(stock["8475HD"])
            continue
        if marca == "Acer":
            print(stock["2175HD"])
            continue
        if marca == "Asus":
            print(stock["JjfFHD"])
            continue
        else:
            print("ingrese una opcion valida!!")
            continue
        

    if opcion == 2:
        precioMi=int(input("ingrese el precio minimo: "))
        precioMa=int(input("ingrese el precio maximo: "))
        
    if opcion == 3:
        int(input("ingrese marca a consultar: "))

    if opcion == 4:
        print("programa finalizado")
        break
    else :
        print("ingrese una opcion valida!!")
        continue