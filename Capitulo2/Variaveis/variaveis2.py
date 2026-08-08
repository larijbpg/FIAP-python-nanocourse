"""Declaro para o senhor Gonçalves Dias que o senhor Humberto Delgado esteve presente no evento SecurityCup e gastou o valor de R$ 30,00 com a entrada."""

responsavel = input('Digite o nome do responsável:')
funcionario = input('Digite o nome do funcionario:')
evento = input('Digite o nome do evento:')
valor_entrada = float(input('Digite o valor da entrada:'))

print('Declaro para o senhor ' + responsavel + ', que o senhor ' + funcionario + 'esteve presente no evento ' + evento + 'e gastou o valor de R$ ' + str(valor_entrada) + 'com a entrada')