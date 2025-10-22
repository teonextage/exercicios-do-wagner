def imposto(preco):
    produto = preco + (preco * 0.15) 
    return produto

preco_Produto = float(input("Digite o preco do produto: "))
resposta = imposto(preco_Produto)
print("Seu produto custa",resposta)