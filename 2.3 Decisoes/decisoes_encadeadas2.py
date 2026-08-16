
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA") #independente da idade e do genero, ela vai pra sala amarela se a condição for verdadeira
elif doenca_infectocontagiosa=="NAO":
    print("Encaminhe o paciente para sala BRANCA")
else: #se a informação nao estiver dentro do esperado, o usuario deverá ser informado de que foi impossiel definir a sala
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO: prioridade
if idade >= 65:
    print("Paciente COM prioridade")
else: #se tiver menos que 65 ainda n da pra definir, pois pode ser uma mulher grávida
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")