# Questão 1 - Modulacao de strings e words

frase = input("Digite uma frase:")
palavra = input("Digite uma palavra para buscar:")

frase_minuscula = frase.lower()
palavra_minuscula = palavra.lower()
palavra_frase = frase_minuscula.split()
quantidade = 0

def search_words(word, phrase, quant):
    for p in phrase:
        if p == word:
            quant += 1
    return quant

quantity = search_words(palavra_minuscula, palavra_frase, quantidade)
print("Existe(m)",quantity,"palavra(s)")

