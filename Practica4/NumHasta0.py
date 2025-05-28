while True:
    print("\n\nEn este programa tendras que ingresar un número y\nte mostrará la cuenta regresiva hasta 0")
    try:
        num = int(input("\nIngresa un numero: "))
        if num <= 0:
            print("Error : ingresa un numero valido.")
        else:
            for i in range(num, -1, -1):
                print(i, ",")
    except ValueError:
        print("Error: Debes escribir un número entero válido.")
    seguir = input("¿Quieres probar otro número? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa.")
        break