import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def main():
    #Aqui vai a frase/ entrada do usuário/ base de dados. Por agora será uma frase pré definida para testes
    frase = "O dia está bonito hoje"

    #Eu tenho que limpar o texto para treinar o modelo
    #Nisso irei tirar pontuação, stop-words(palavras que não tem tanto significado) e uniformizar o texto(deixar tudo minúsculo)
    #Nisso tenho que tokenizar o texto(é praticamente transformar cada palavra/pontuação em um elemento de uma lista)
    palavras = word_tokenize(frase.lower(), language="portuguese")

    #Carrego as stop-words da biblioteca
    stop_words = set(stopwords.words('portuguese'))

    #Removo as stop-words
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_words]

    print(palavras_filtradas)
    return





if __name__ == "__main__":
    main()
