try:
    numerador = float(input("Digite o (numerador) da divisao: "))
    denominador = float(input("Digite o (denominador) da divisao: "))
    resultado = numerador / denominador
    print(f"O resultado da divisao é {resultado}")
    
except ZeroDivisionError:
    print("Não é possivel dividir por zero!")