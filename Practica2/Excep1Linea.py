try:
    numero = int(input("Escrube un numero entre el 1 y el 9: "))
    resultado = 100 / numero
    print ("El resultado es: ", resultado)
except (ValueError, ZeroDivisionError):
    print("Error: Debes escribir un numero valido mayor a 0") 