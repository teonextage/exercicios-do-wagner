import conversor

print("Conversor de temperatura")
print("1 - Celsius para Fahreheit")
print("2 - Fahreheit para Celsius")
opcao = int(input("Escolha uma opcao: (1 ou 2):"))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius:"))
    resultado = conversor.celsius_para_fahrenheit(celsius)
    print(f"{celsius}*C erquivale a {resultado:.2f}*F")
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahreheit:"))
    resultado = conversor.fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}*F erquivale a {resultado:.2f}*C")
else:
    print("Opção inválida")   