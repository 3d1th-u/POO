while True:
    """se usa para ejecutar un bloque de código repetidamente hasta que una 
    condición booleana dada y se evalúa como False"""
    try:
        print("\n\nEn este programa ingresas un número y devuelve si es par o impar")
        num = int(input("Escribe un número: "))
        if num < 1:
             print("ERror: Ingresa un número válido.")
        else:
            if num % 2 == 0:
                print("El número", num, "es par.")
            else:
                print("El número", num, "es impar.")
    except ValueError:
        print("Error: Debes escribir un número entero válido.")
    seguir = input("¿Quieres probar otro número? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa.")
        break