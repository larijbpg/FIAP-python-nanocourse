usuarios = {} #dicionario de dados com chaves {}
usuarios = {'Chaves': ['Chaves Silva', '17/06/2017', 'Recep_01'], #login como chave de cada objeto: dados do objeto, como sao varios, foi feito dentro de uma lista
            'Quico': ['Enrico Flores', '03/06/2017', 'Raiox_02'] # segundo objeto
            }

# Adicionando um item no dicionario
usuarios['Florinda']=['Florinda Flores', '26/11/2017', 'Recep_01']
# colocamos entre [] o dado que sera armazenado e iguaamos com o dado que pertence à chave

# ====================================================================================================

# Se eu tentar acrescentar esses usuarios, ele vai acrescentar apenas 3, ou seja:
    # chaves, quico 'raiox_03' e florinda '2016', pq foram os ultimos acessados e vai apagar os anteriores.
usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    }
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios) # podemos ver tudo oq existe no dicionario e perceber que ele deixa apens o ultimo login daquele usuario
print(100*'=')
print('Dados: ', usuarios.get('Chapolim')) # quero que mostre: pegue os objetos que estao na chave 'Chaves' no dicionario usuarios
# se eu escrever 'Chapolim' ele retorna None, pois não existe uma chave com esse nome.