from Funcoes_Dicionarios import * # importo tudo o que está dentro do arquivo Funcoes_Dicionarios

usuarios = {}

opcao = perguntar()
while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        inserir(usuarios)
    if opcao == 'P':
        pesquisar(usuarios, input('Qual login deseja pesquisar? '))
    if opcao == 'E':
        excluir(usuarios, input('Qual código de lançamento deseja excluir? '))
    if opcao == 'L':
        listar(usuarios)
    opcao = perguntar()