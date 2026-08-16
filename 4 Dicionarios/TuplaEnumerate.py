usuarios = {} # dicionario para usuarios
resp = "S"
# quero que o email do usuario esteja como chave do dicionario 
# e os outros dados (nome, nível) fiquem como os dados do dicionario no formato de lista
# o problema é que os emails podem ser repetidos, por isso precisamos enumera-los e por isso colocamos eles em uma lista
emails = [] 
while resp == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

# gerar tuplas, formadas por numero sequencial e o email para depois adicionar a tupla como chave do dicionario

tupla = list(enumerate(emails)) #enumerando(enumerate()) cada item encontrado na lista emails e gerando uma tupla com cada elemento (list())
for chave in range(0,len(tupla)): #para cada chave na lista TOTAL(range()) da tupla
    print("Email: ", tupla[chave][1]) # exibir o email[1] que recebera o nome e o nivel da tupla 
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

# {( 0, "email") : ["nome","nível"]} dicionario => tupla[0][1] : lista[0][1]

print("="*50)

for chave, dado in usuarios.items():
    print("Usuario.: ", chave[0])
    print("Email...: ", chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])