"""Servem para avaliarmos uma situação e, dependendo da situação, serão tomadas algumas outras decisões"""

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

"""Existem duas condições: idades e suspeita de doença infecto-contagiosa. Não faz muita iferença qual decisao usar. 
Porem, se tivessemos mais condições, seria muitos if e elif, portanto
por questões de boa prática, é melhor usar decisções encadeadas"""