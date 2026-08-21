
import sys
sys.path.append(".")
from Funcoes.Funcoes_Arquivos import *

inventario = {} #cria um dicionario de dados chamado inventario
opcao = chamarMenu()
while opcao > 0 and opcao <= 4: #enquanto o usuario digitar qualquer um dos numeros o programa continuara, se for outro valor, o programa sera encerrado
    if opcao == 1: # se digitar 1 ele entrará no laço "while" e enquanto ele digitar "s", continuara adicionando itens no dicionario
        registrar(inventario)
    elif opcao == 2: #considerando que foi 2, ira abrir o arquivo csv em modo concatenação e entao para cada objeto encontrado no dicionario, iremos adicionar uma linha no arquivo
        persistir(inventario)
    elif opcao == 3:
        for linha in exibir():
            print(linha.strip())
        resultado = exibir() # atribuimos para a variável resultado os dados que foram retornados pela função exibir(), ou seja, o conteudo do arquivo "inventario.csv" em forma de lista
        for linha in resultado: # mantem o for para percorrer toda a lista, pq nao queremos que saia o numero do patrimonio em todos os ativos
            # print(linha[2:-1]) # de cada linha, vai exibir apenas o caractere [2] até o ultimo [-1]
                    # "[2:-1]" => SLICE => RECORTE EM UMA STRING => quero o caractere 2 até o final
                    # tomar cuidado pois pode vir oq não desejo, portanto 
            # separacao = linha[linha.find(";") + 1 : -1] # irá retornar a posição do primeiro ";", encontrado e então acrescentará +1para que nao exiba o ; na saída
            # data = separacao[0:separacao.find(";") +1 : -1]
            # separacao = separacao[separacao.find(";") +1 : -1]
            # descricao = separacao[0: separacao.find(";") +1 : -1]
            # departamento = linha[linha.rfind(";") +1 : -1]
            # # rfind() faz leitura da direita para a esquerda
            # print("Data..........: ", data)
            # print("Descrição.....: ", descricao)
            # print("Departamento..: ", departamento)
            # TUDO ISSO NÃO É PRATICO FAZER, IMAGINA SE EU TIVESSE 40 DADOS (aqui foram 3 - data, descrição e departamento)
            # para isso temos o SPLIT() => gera uma lista, e, em cada posição, teremos uma parte da string, de acordo com a quebra que foi proposta
            lista = linha.split(";")
            print("Data..........: ", lista[1])
            print("Descrição.....: ", lista[2])
            print("Departamento..: ", lista[3])
    elif opcao == 4:
        dep = input("Digite o nome do departamento que deseja pesquisar: ")
        buscar_por_departamento(dep)

    opcao = chamarMenu()
