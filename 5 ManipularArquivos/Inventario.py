"""
Armazenar apenas os seguintes dados: o nº patrimonial do ativo, descrição do ativo, data da ulima atualização e o nome
do departamento em que esta lozalizado. Primeiro, iremos definifir uma estrutura de dados para armazena-lo, 
eles serão recebidos pelo colaborador responsavel por catalogar os ativos e, entao, persistiremos os dados para um arquivo, 
para que possam ser recuperados, "backupeados", alterados, excluidos e estejam disponiveis pra qualquer outra 
consulta que possa ser necessaria posteriormente.
"""
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
    elif opcao == 4:
        dep = input("Digite o nome do departamento que deseja pesquisar: ")
        buscar_por_departamento(dep)

    opcao = chamarMenu()
