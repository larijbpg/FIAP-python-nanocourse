ips = {} # criamos um dicionário chamado "ips"
resp = "S" # criamos uma variável chamada "resp" para controlar o laço
while resp == "S": # dentro do laço de repetição vamos preencher o dicionário
    ips[(input("Digite os dois primeiros octetos: "), # na chave vamos inserir dois valores (primeira parte do ip e segunda parte do ip) dentro de uma tupla
        input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite <S> para continuar: ").upper()
        # IP 172.168.5.2 = Nome da máquina
print("Exibindo ip's: ")
for ip in ips.keys(): #ele vai pegar somente as chaves do dicionario em formato de lista
    print(ip[0] + "." + ip[1]) #ips concatenados com "."
    # 172.1168


print("Exibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ") # armazenando o dado(máquina) na variável pesquisa
for ip, nome in ips.items(): #recuperar dois dados ip e o nome da máquina, que serão retornados pelo método items()
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1] == pesquisa): #comparação da parte dois do ip com oq o usuario digitou na variavel pesquisa e se forem iguais será exibido o nome da máquina
        print(nome)


# para saber quais estações compoem uma rede
# Para isso vamos nos basear nos dois primeiros octetos do ip
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items(): 
# recebe os dois valores do dicionario(chave e dado). 
# Como a chave é tupla com 2 valores, pegamos o primeiro valor para comparar com o conteudo da variavel "rede"
    if (ip[0] == rede): # se forem iguais, exibimos os nomes das estações que compõem ou que estao "penduradas" na rede que foi especificada pelo usuario
        print(nome)