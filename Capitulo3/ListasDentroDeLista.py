# Vou criar duas listas: inventario(lista externa) e equipamentos (lista interna)
# Função de adicionar 
inventario = []

resposta = 'S'
while resposta == 'S':
    equipamento = [input('Equipamento: '),
                    float(input('Valor: ')),
                    int(input('Numero serial: ')),
                    input('Departamento: ')]
    inventario.append(equipamento) # adicionei a lista equipamento dentro da lista inventario
    resposta = input('Digite "S" para continuar: ').upper() # se quiser adicionar mais equipamentos, só digitar s


for elemento in inventario:
    print('Nome...........: ', elemento[0])
    print('Valor..........: ', elemento[1])
    print('Serial.........: ', elemento[2])
    print('Departamento...: ', elemento[3])


busca = input('Digite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor..: ', elemento[1])
        print('Serial.: ', elemento[2])


depreciacao = input('Digite o nome do equipamento que será depreciado: ')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Novo valor: ', elemento[1])


serial = int(input('Digite o serial do equipamento que será excluido: '))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)


for elemento in inventario:
    print('Nome...........: ', elemento[0])
    print('Valor..........: ', elemento[1])
    print('Serial.........: ', elemento[2])
    print('Departamento...: ', elemento[3])


#crio uma lista para adicionar apenas os valores dos equipamentos
valores = [] 

for elemento in inventario:
    valores.append(elemento[1]) #adiciono todos os valores da posição [1] -> posição de valor das listas
if len(valores)>0: # se existir no minimo um valor dentro da lista, as funções serão executadas:
    print('O equipamento mais caro custa: ', max(valores)) # maior valor numerico
    print('O equipamento mais barato custa: ', min(valores)) # menor valor numerico
    print('O total de equipamentos é de: ', sum(valores)) # total entre os valores

