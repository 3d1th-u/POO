while True:
        print("\n\nEste programa te dice siuna palabra es un palímdromo")
        palabra = input("\nIngresa una palabra o una frase (¡en letras minusculas!): ")
        palabrasinespacios = palabra.replace(" ","")
        if palabrasinespacios == palabrasinespacios[::-1]:
            print("\n", palabra, "¡Si es un palindromo!")
        else:
            print("\n", palabra, "¡No es un palindromo!")
            
        seguir = input("\n¿Quieres probar otro número? \n (Utiliza 0 para NO y 1 para SÍ): ")
        if seguir != "1":
            print("Fin de la ejecución del programa.")
            break