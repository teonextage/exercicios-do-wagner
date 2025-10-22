def maior_ou_menor(idade):
    if idade >= 18:
        return "Maior de idade!"
    else:
        return "Menor de idade"

idade = int(input("Digite a sua idade: "))
resultado = maior_ou_menor(idade)
print(resultado)