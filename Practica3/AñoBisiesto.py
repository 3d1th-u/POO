while True:
    try:
        print("\n\n Este programa te dice si un año es bisiesto:")
        año = int(input("\nIngresa un año (por ejemplo 2024):"))
        if año % 4 == 0 and año % 100 != 0 or año % 100 == 0:
            print("¡El año ", año, "es bisiesto!")
        else:
            print("¡El año ", año, "no es bisiesto!")
    except ValueError:
        print("Error: Debes escribir un año válido.")
    seguir = input("¿Quieres probar con otro año? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa.")
        break