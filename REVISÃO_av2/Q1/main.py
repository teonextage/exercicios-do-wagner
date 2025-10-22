def autenticar(email, senha):
    if email == 'admin' and senha == 'admin':
        return True
    else:
        return False

email = input("Digite um email: ")
senha = input("Digite uma senha: ")
resultado = autenticar(email, senha)
print(resultado)