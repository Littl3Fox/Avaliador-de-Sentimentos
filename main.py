import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def main():
    #Aqui vai a frase/ entrada do usuário/ base de dados. Por agora será uma frase pré definida para testes
    dataset = open("dataset.txt","r",  encoding="utf-8")

    #Carrego as stop-words da biblioteca
    stop_words = set(stopwords.words('portuguese'))

    #Eu tenho que limpar o texto para treinar o modelo
    #Nisso irei tirar pontuação, stop-words(palavras que não tem tanto significado) e uniformizar o texto(deixar tudo minúsculo)
    #Nisso tenho que tokenizar o texto(é praticamente transformar cada palavra/pontuação em um elemento de uma lista)
    frases = []

    for linha in dataset:

        #Divido o texto do rótulo
        texto, sentimento = linha.split(";")
        sentimento = sentimento.strip()

        #Transformo as palavras em minusculas e token
        tokens = word_tokenize(texto.lower(), language="portuguese")

        #Tiro stopwords da frase e pontuação
        tokens_filtrados = [palavra for palavra in tokens if palavra not in stop_words and palavra not in string.punctuation]

        #Faço uma lista de dicionario com a frase e seu respectivo sentimento
        frases.append({
            "frase": tokens_filtrados,
            "sentimento": sentimento
        })

    

    print(frases)

    
    return





if __name__ == "__main__":
    main()
