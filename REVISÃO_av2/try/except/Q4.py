def dividir(a, b):
    return a / b

try:
    a = float(input("Digite o primeiro numero da divisao:"))
    b = float(input("Digite o segundo numero da divisao: "))
    resultado = dividir(a, b)
    print(f"O resultado da divisao é {resultado}. ")
    
except ZeroDivisionError:
    print("Nao se deve dividir por zero!")

except ValueError:
    print("Voce nao digitou um numero!")