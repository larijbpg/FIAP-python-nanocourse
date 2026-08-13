# criei esse arquivo de funções pois percebi que no codigo estou repetindo funções(tendo que digita-las algums vezes)
# posso colocar essas funções aqui e só chama-las lá no código do arquivo ManagerUser(virou meu Módulo Principal)
    # primeiro vou importar essas funções daqui pra lá
    # depois tenho que chama-las

def perguntar():
    resposta = input('O que deseja realizar?'
                + '<I> - Para Inserir um usuário' 
                + '<P> - Para Pesquisar um usuário'
                + '<E> - Para Excluir um usuário'
                + '<L>' - 'Para Listar um usuário: ').upper()
    return resposta

def inserir(dicionario):
    dicionario[input('Digite o login: ').upper()] = [input('Digite o nome: ').upper(),
                                                     input('Digite a última data de acesso: '),
                                                     input('Digite a última estação acessada: ').upper()]