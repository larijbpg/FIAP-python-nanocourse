nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
prioridade = 'NÃO'

if idade >= 65:
    prioridade = 'SIM' # o código irá mudar o valor da vriavel 'prioridade' de acordo com o valor da idade
print('O paciente ' + nome + ' possui atendimento prioritário? ' + prioridade)
