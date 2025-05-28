while True:
    print("\n\nEste programa un número entero positivo mayor de 10 y\n te muestra como resultado todos los números impares desde 2 hasta ese número")
    try:
        num = int(input("\nEscribe un número positivo mayor a 10: "))
        if num  <= 10:
            print("Error: Ingresa un numero váliddo.")
        else:
            for i in range (2, num+1):
                if i % 2 != 0:
                    print(i, ",")
    except ValueError:
        print("Error: Debes escribir un número entero válido.")
    seguir = input("¿Quieres probar otro número? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa.")
        break