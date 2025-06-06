while True:
    print("\n\nEn este programa tendras que ingresar un número\nentre 200 y400, este programa lo que hara es que\nte mostrará todos los numeros pares en la serie entre el número y el 400")
    try:
        num = int(input("\Ingresa un número entre 200 y 400: "))
    
        if num < 200:
            print("Error: ingresa un número valido en el rango.")
    
        else:
            for i in range ( num, 402):
                if i % 2 == 0:
                    print(i, ",")
            
    except ValueError:
        print("Error: Debes escribir un número entero válido.")
    seguir = input("¿Quieres probar otro número? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa :]")
        break