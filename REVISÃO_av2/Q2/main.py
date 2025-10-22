def desconto(juros):
    juros = preco - (juros * 0.10)
    return juros

preco = float(input("Digite um preco de um produto: "))
resultado = desconto(preco)
print(resultado)