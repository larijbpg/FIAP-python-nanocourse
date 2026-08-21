import getpass
from datetime import datetime


# print("Usuário.......: ", getpass.getuser()) # usuario
# print("="*100)
# print("Data Completa.: ", datetime.now()) #data completa
# print("="*100)
# print("Dia...........: ", datetime.now().day) #dia
# print("="*100)
# print("Mês...........: ", datetime.now().month)
# print("="*100)
# print("Ano...........: ", datetime.now().year)
# print("="*100)
# print("Hora..........: ", datetime.now().hour)
# print("="*100)
# print("Minuto........: ", datetime.now().minute)
# print("="*100)
# print("Segundo.......: ", datetime.now().second)
# print("="*100)

usuario = input("Digite o usuário: "). upper()
senha = input("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Usuário Negado")
# mas a senha aparecerá na tela, PORTANTO... dá pra usar outra função do getpass (arquivo Login.py)
