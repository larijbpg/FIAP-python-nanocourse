from Capitulo4.Funcoes import * # importo tudo o que está dentro do arquivo Funcoes

usuarios = {}
opcao = input('O que deseja realizar?'
               + 
                '<I> - Para Inserir um usuário' 
                + '<P> - Para Pesquisar um usuário'
                + '<E> - Para Excluir um usuário'
                + '<L>' - 'Para Listar um usuário: ').upper()

while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
    if opcao == 'I':
        # chave = input('Digite o login: ').upper()
        # nome = input('Digite o nome: ').upper()
        # data = input('Digite a última data de acesso: ')
        # estacao = input('Digite a utima estação acessada: ').upper()
        # usuarios[chave] = [nome, data, estacao]
                        
                        # OU ECONOMIZANDO 2 LINHAS
        # chave = input('Digite o login: ').upper()                
        # usuarios[chave] = [input('Digite o nome: ').upper(),
        #                    input('Digite a ultima data de acesso: '),
        #                    input('Qual a última estação acessada: ').upper]
                        
                        # OU UMA LINHA SÓ
        usuarios[input('Digite o login: ').upper] = [input('Digite o nome: ').upper(),
                                                     input('Digite a última data de acesso: '),
                                                     input('Dgite a última estação acessada: ').upper()]
    opcao = input('O que deseja realizar?'
               + 
                '<I> - Para Inserir um usuário' 
                + '<P> - Para Pesquisar um usuário'
                + '<E> - Para Excluir um usuário'
                + '<L>' - 'Para Listar um usuário: ').upper()