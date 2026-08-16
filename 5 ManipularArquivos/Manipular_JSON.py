import sys

from Funcoes_JSON import *

caminho_arquivo = "FIAPPython/5 ManipularArquivos/inventario_json.json"

inventario = ler_arquivo(caminho_arquivo)
opcao = chamarMenu()

while opcao > 0 and opcao < 3:
    if opcao == 1:
       print(registrar(inventario, caminho_arquivo))
    elif opcao == 2:
        exibir(caminho_arquivo)
    opcao = chamarMenu()
