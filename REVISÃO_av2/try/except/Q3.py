try:
    numerador = float(input("Digite o primeiro numero (numerador): "))
    denominador = float(input("Digite o segundo numero (denominador):"))
    resultado = numerador / denominador
    print(f"O resultado da divisao é {resultado}.")
    
except ValueError:
    print("O que voce digitou nao é valido")
    
except ZeroDivisionError:
    print("Nao é possivel dividir por zero!")