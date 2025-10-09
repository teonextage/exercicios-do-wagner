# Verificacao de numero par ou impar

numero = int(input("Digite um numero par ou impar: "))

def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
resposta = par_ou_impar(numero)
print(resposta)
        

