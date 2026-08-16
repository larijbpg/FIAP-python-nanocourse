# criei esse arquivo de funções pois percebi que no codigo estou repetindo funções(tendo que digita-las algums vezes)
# posso colocar essas funções aqui e só chama-las lá no código do arquivo ManagerUser(virou meu Módulo Principal)
    # primeiro vou importar essas funções daqui pra lá
    # depois tenho que chama-las

def perguntar():
    resposta = input('O que deseja realizar?'
                + '<I> - Para Inserir um usuário' 
                + '<P> - Para Pesquisar um usuário'
                + '<E> - Para Excluir um usuário'
                + '<L> - Para Listar um usuário: ').upper()
    return resposta

def inserir(dicionario):
    dicionario[input('Digite o código do lançamento: ').upper()] = [input('Digite o login: ').upper(), 
                                                                    input('Digite o nome: ').upper(),
                                                                    input('Digite a hora: ').upper(),
                                                                    input('Digite a última data de acesso: '),
                                                                    input('Digite a última estação acessada: ').upper(),
                                                                    input('Digite o nível do usuário: ').upper()]

def pesquisar(dicionario, chave): #precisamos receber o dicionario onde vamos pesquisar e a chave que tem o dado que será pesquisado
    lista = dicionario.get(chave) # preencher uma lista com o resultado da pesquisa
    if lista != None: # caso a lista não esteja vazia (!=None) vamos exibir os 3 dados que compoe a lista
        print('Login...............: ' + lista[0])
        print('Nome: ..............: ' + lista[1])
        print('Hora................: ' + lista[2])
        print('Último acesso.......: ' + lista[3])
        print('Última estação......: ' + lista[4])
        print('Nível do usuário....: ' + lista[5])


def excluir (dicionario, chave):
    if dicionario.get(chave) != None: # antes de excluir preciso saber se existe a chave. Se o .get() retornar algo diferente de vazio:
        del dicionario[chave] # vai deletar o objeto de acordo com  chave que foi recebida
    print('Objeto Eliminado')


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Objeto.....')
        print('Código de lançamento: ', chave)
        print('Dados: ', valor)
