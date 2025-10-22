try:
    numero = int(input("Digite um numero: "))
    print(f"O numero que voce digitou foi {numero}")
    
except ValueError:
    print("Voce nao digitou um numero!")