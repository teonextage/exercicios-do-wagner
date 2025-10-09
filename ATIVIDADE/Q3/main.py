# SISTEMA DE AUTENTICAÇÃO SIMPLES
# USUÁRIOS E SENHAS JA PRÉ DEFINIDOS


usuarios = {
    "admin" : "123",
    "teo" : "5644",
    "joao" : "senha123"
}

def autenticar():
    usuario = input("Usuário:")
    senha = input("Senha:")
    if usuarios.get(usuario) == senha:
        print("Autenticação bem-sucedida!")
    else:
        print("usuario ou senha incorretos!")
        
autenticar()