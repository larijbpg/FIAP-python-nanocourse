
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'

while resposta == 'S': 
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Numero serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite "S" para continuar: ').upper()

# toda vez que cadatrar um item, vou colocar todas essas informações, portanto, todas as listas terão o mesmo tamanho!

for indice in range(0, len(equipamentos)): # <-- Aqui ele só define: "Vou rodar usando o índice 0, depois 1, depois 2..."
    print('Equipamento..:', (indice+1)) #quero que ele mostre o indice desse item na lista
    print('Nome.........: ', equipamentos[indice])
    print('Valor........: ', valores[indice])
    print('Serial.......: ', seriais[indice])
    print('Departamento.: ', departamentos[indice])
    # para cada indice na sequencia de 0 até o numero de itens que tem na lista equipamentos, mostre todos esses prints:

    # O for não vai passear pelos nomes dos equipamentos diretamente. 
    # Ele vai passear pelas posições numéricas (0, 1, 2...), de zero até o tamanho total da lista.

# ==============================================================================================================================================


# Agora quero pesquisar um determinado dado:

busca = input('Digite o nome do equipamento que deseja buscar: ')

for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor...: ', valores[indice])
        print('Serial..: ', seriais[indice] )
# Para cada número de índice (0, 1, 2...) na sequência de 0 até a quantidade de itens da lista equipamentos:
# Se o que eu digitei for igual ao indice da vez da lista equipamentos:
# use ESSE MESMO numero[indice] para ir buscar o preço certo na lista valores e o serial certo na lista seriais

# ==============================================================================================================================================


# Montar um codigo que será responsavel por depreciar(desvalorização após certo periodo) de 10%.

depreciacao = input('Digite o nome do equiapmento que será depreciado: ')

for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print('Valor antigo: ', valores[indice])
        valores[indice] = valores[indice] * 0.9 # estou substituindo o antigo valor
        print('Novo Valor: ', valores[indice])

# ==============================================================================================================================================

# Deletar um item da lista:

serial = input('Digite o serial do equiapmento que será excluido: ')

for indice in range(0, len(departamentos)):
    if seriais[indice] == serial: #se ele achar esse indice, ele vai excluir o mesmo indice em todas as seguintes listas:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break 
            # break: força o fim do laço 'for' e 'while' -> eficiencia (não gasta tempo à toa) e 
            # evita erro de contagem, pq agr os indices mudarem

for indice in range(0, len(equipamentos)):
    print('Equipamento..: ', (indice+1))
    print('Nome.........: ', equipamentos[indice])
    print('Valor........: ', valores[indice])
    print('Serial.......: ', seriais[indice])
    print('Departamento.: ', departamentos[indice])