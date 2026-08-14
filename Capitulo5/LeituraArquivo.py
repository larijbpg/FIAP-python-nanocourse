with open('teste.txt', 'r') as arquivo: #abra o arquivo teste.txt para leitura e atribui para a variavel 'conteudo'
    conteudo = arquivo.readlines() # todo o conteudo do arquivo é atribuido à variavel conteúdo
print('Tipo de dado da variável', type(conteudo))
print('Conteúdo do arquivo: ', conteudo)