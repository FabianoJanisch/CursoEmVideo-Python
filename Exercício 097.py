def escreva(palavra):
    tamanho = len(palavra) + 4
    print (tamanho*'-')
    print (palavra.center(tamanho))
    print (tamanho*'-')


escreva('Olá, Mundo!')
escreva('Curso de Python maneiro')
escreva('Muito legal mesmo cara')