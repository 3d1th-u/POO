while True:
    print("\n\nEste programa ingresasuna frase y una kletra, luego \n te muestra como resultado cuantas letras hay en esa frase ")
    
    frase = input("\nIngresa una frase: ")
    letra = input("\nIngreasa una letra: ")
        
    if len(letra) != 1:
        raise ValueError("Debes ingresar solamente una letra.")
    
    contrador = 0
        
    for letrita in frase:
        if letrita == letra:
            contrador += 1
                        
    print("\nLa letra ", letra, "aparece ", contrador, "veces en la frase", frase)
    seguir = input("¿Quieres probar otra frase? \n (Utiliza 0 para NO y 1 para SÍ): ")
    if seguir != "1":
        print("Fin de la ejecución del programa.")
        break