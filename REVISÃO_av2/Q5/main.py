def calculo_IMC(altura, peso):
    IMC = peso / (altura **2)
    return IMC

def classfificacao(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"
    
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

Imc = calculo_IMC(peso, altura)
Medida = classfificacao(Imc)

print(Imc)
print(Medida)