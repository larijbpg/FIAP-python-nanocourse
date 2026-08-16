inventarios = []
resposta = 'S'
while resposta == 'S':
    inventarios.append(input('Equipamento: '))
    inventarios.append(float(input('Valor: ')))
    inventarios.append(int(input('Numero serial: ')))
    inventarios.append(input('Departamento: '))
    resposta = input('Digite "S" para continuar: ').upper()

for inventario in inventarios: #estrutura foreach permite definir um nome para cada elemento qu ele encontrar na lista. Chamei de inventario
    print(inventario)