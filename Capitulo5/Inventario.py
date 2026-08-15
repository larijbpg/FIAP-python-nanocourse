"""
Armazenar apenas os seguintes dados: o nº patrimonial do ativo, descrição do ativo, data da ulima atualização e o nome
do departamento em que esta lozalizado. Primeiro, iremos definifir uma estrutura de dados para armazena-lo, 
eles serão recebidos pelo colaborador responsavel por catalogar os ativos e, entao, persistiremos os dados para um arquivo, 
para que possam ser recuperados, "backupeados", alterados, excluidos e estejam disponiveis pra qualquer outra 
consulta que possa ser necessaria posteriormente.
"""

inventario = {} #cria um dicionario de dados chamado inventario
opcao = int(input("Digite: " 
                    "<1> para registrar ativo"
                    "<2> para persistir em arquivo"
                    "<3> para exibir ativos armazenados: "
                    "<0> para SAIR"
                  )) 
while opcao > 0 and opcao < 4: #enquanto o usuario digitar qualquer um dos numeros o programa continuara, se for outro valor, o programa sera encerrado
    if opcao == 1: # se digitar 1 ele entrará no laço "while" e enquanto ele digitar "s", continuara adicionando itens no dicionario
        resp = "S" # garantir a entrada no loop/ chave de ignição para o loop rodar a primeira vez, visto que a opcao foi 1
        while resp == "S": # considerando que a resposta foi sim (ja que digitou 1)
            inventario[input("Digite o numero patrimonial: ")] = [
                        input("Digite a data da ultima atualização: "),
                        input("Digite a descrição: "),
                        input("Digite o departamento: ")
            ]
            resp = input("Digite <S> para continuar").upper() #se for sim, volta pro "while.."
    elif opcao == 2: #considerando que foi 2, ira abrir o arquivo csv em modo concatenação e entao para cada objeto encontrado no dicionario, iremos adicionar uma linha no arquivo
        with open("Capitulo5/inventario.csv", "a") as inv: # "a" pois caso nao ter o arquivo, posso criar do zero
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n") 
                # usei "; pq no excel ele entende que cada ; é uma coluna diferente e quebra de linha no final para o Excel saber que na sequencia tem outro valor
                print("Persistido com sucesso!")
    elif opcao == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines()) #abrir em modo leitura e com o readlines() irá mostrar todas as linhas
    opcao = int(input("Digite: "
                      "<1> para registrar ativo"
                      "<2> para persistir em arquivo"
                      "<3> para exibir ativos armazenados: "
                      ))
