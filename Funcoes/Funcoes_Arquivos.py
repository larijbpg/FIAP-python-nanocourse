def chamarMenu():
    escolha = int(input("Digite: "
                       "<1> para registrar ativo"
                       "<2> para persistir em arquivo"
                       "<3> para exibir ativos armazenados: "
                       "<4> para buscar por departamento: "
                       ))
    return escolha

def registrar(dicionario):
    resp = "S"
    while resp =="S":
        dicionario[input("Digite o numero patrimonial: ")] = [input("Digite a data da última atualização: "),
                                                              input("Digite a descrição: "),
                                                              input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items(): # retornar como tupla chave: valor
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n") # NúmeroPatrimonial;Data;Descrição;Departament
    return "Persistido com sucesso!"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas

def buscar_por_departamento(dep_alvo):
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()

    print(f"\n--- ATIVOS DO DEPARTAMENTO: {dep_alvo.upper()} --- ")
    encontrado = False

    for linha in linhas:
        # remove a quebra de linhas '\n' e separa pelas colunas ';'
        dados = linha.strip().split(";")

        #supondo a estrutura: [numero de serie, nome/descrição, valor, departamento]
        # o departamento está no indice 3 (dados[3]), portanto
        if len(dados) >=4 and dados[3].upper() == dep_alvo.upper():
            print(f"Série: {dados[0]} | Descrição: {dados[2]} | Data: {1}")
            encontrado = True

    if not encontrado: 
        print("Nenhum ativo encontrado para este departamento.")
    print("-"*50)