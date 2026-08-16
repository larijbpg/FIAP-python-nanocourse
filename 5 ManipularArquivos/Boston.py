"""
Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?
Quando (mes/ano)(coluna 0 e 1) ocorreu o maior transito de passageiros no aeroporto Logan? -> coluna 2 do arquivo
Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for especificado pelo usuario? -> vou usar input
Qual o mês que possui a maior media da diária de um hotel, com base no ano especificado pelo usuario -> vou usar input
"""
# Primeiro: abro o arquivo em modo de leitura
with open("FIAPPython/5 ManipularArquivos/economic-indicators.csv", 'r') as boston: 

# crio variaveis zeradas para quando for comparar linha por linha não dar erro
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuário = input("Qual ano deseja pesquisar? ")

# loop "foreach" para percorrer somente da linha 1 ate a ultima, a 0 não pq são os títulos
    for linha in boston.readlines()[1 :]: # primeira linha completa do arquivo = 2013,1,2019662,2986,0.572,158.93,322957,0.066,0.631,329,80000000,313107,228,44,11,380000,405,534,134
        lista = linha.split(",") # o que o split(",") faz: ['2013']['1']['2019662']['2986']['0.572']['158.93'][322957][0.066][0.631][329][80000000][313107][228][44][11][380000][405][534][134]
        if lista[0] == "2014": # quero que seja apenas do ano 2014!
            total_voos = total_voos + float(lista[3]) # agora ele vai pegar apenas o item[3] de cada linha => [2019662.0], deixa float para evitar erros, caso a tabela venha com numero decimal 259.0
        if float(lista[2]) > float(maior): #se o valor da coluna 2 (na linha atual) for maior que o valor da variavel "maior":
            maior = lista[2] # novo valor da variavel maior
            ano = lista[0] # novo valor para a variavel ano
            mes = lista[1] # novo valor para a variavel mes
        if ano_usuário == lista[0]: # se o ano escolhido pelo usuario for igual ao da coluna 0:
            total_passageiros = total_passageiros + float(lista[2])
        if float(lista[5]) > float(maior_media_diaria):
            maior_media_diaria = float(lista[5])
            mes_maior_diaria = lista[1]

    print("O total de voos internacionais que partiram do aeroporto de Logan é ",total_voos)
    print("="*100)
    print("O mês/ano de maior movimento no aeroporto foi: ", str(mes),"/", str(ano))
    print("="*100)
    print("O total de passageiros do ano ",ano_usuário, "foi de ",total_passageiros)
    print("="*100)
    print(f"O mês do ano {ano_usuário} com maior média diária de hotel foi {mes_maior_diaria}")
