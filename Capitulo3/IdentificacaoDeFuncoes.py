# ================================================================================================================================

# O identificador da função representa uma "ação" -> inserir, exibir, consultar, apagar, calcular..
# o parametro é um dado que será fornecido para que a função possa executar o seu bloco de códigos
    # o nome do parametro não tem qualquer relação com a lista que será criada no modulo principal
# return deve ser usada quando você desejar que a função retorne um valor para o modulo principal
    # Modulo Principal: local onde a função será chamada

# ================================================================================================================================
def preencherInventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamento: '),
                       float(input('Valor: ')),
                       int(input('Numero Serial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite "S" para continuar: ').upper()

def exibirInventario(lista): # a função irá receber a lista, por parametro, e então executara o laço for
    for elemento in lista:
        print('Nome...........: ', elemento[0])
        print('Valor..........: ', elemento[1])
        print('Serial.........: ', elemento[2])
        print('Departamento...: ', elemento[3])

def localizarPorNome(lista):
    busca = input('Digite o equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print('Valor...: ', elemento[1])
            print('Serial..: ', elemento[2])
def depreciarPorNome(lista):
    depreciacao = input('Digite o equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100) #nova formula matematica 
            print('Novo valor: ', elemento[1])
def excluirPorSerial(lista):
    serial = input('Digite o serial do equipamento que será excluido: ')
    for elemento in lista:
        if elemento[2] = serial:
            lista.append(elemento)
    return "Itens escluídos" # retorna uma strind, quando chama-la, devemos chamar dentro de print()
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print('O equipamento mais caro custa: ', max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('O total de equipamentos é de: ', sum(valores))

# MODULO PRINCIPAL:

