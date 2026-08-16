from Capitulo3_Funcoes.IdentificacaoDeFuncoes import * # '*' faz importar todas as funções contidas no from


minhaLista=[]

print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)

print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista)) #pq somente ela tem retorno
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)