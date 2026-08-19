from geopy.geocoders import Nominatim #abre a biblioteca do mapa e traz pro programa a ferramenta responsável por buscar endereços na internet
from Funcoes_JSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent = "wazeyes") 
#a variavel recebe o nominatim se identificando com o nome de aplicativo "wazeyes"
# como tenho arquivo de funcoes para usar em arquivos json vou usar as variaveis com o mesmo nome
# variaveis => "dicionario"

dicionario = ler_arquivo("entrada.json") 
# a variavel "dicionario" recebe o resultado do retorno que a função entrega depois de ler o arquivo(que é um dicionario)
lista = dicionario["endereco"] 
# a variavel lista recebe os avlores da chave "endereco" que está no dicionario(que recebeu o arquivo de enderecos)
endereco = lista[0] + ", " + lista[1] + ", " + lista[3]
# concatenação das partes do endereço separadas por virgulas e espaços para formar um texto completo
location = geolocator.geocode(endereco) 
# variável do tipo string
# localizacao rrecebe o resultado da busca do geolocator na nuvem 
if location:
    saida = {"coordenadas": (location.latitude, location.longitude)} 
    # a variavel saida cria um novo dicionario onde a chave é "coordenada" e o valor é uma tupla com a latitude e longitude extraídas do objeto location.
    gravar_arquivo(saida, "saida.json") 
    # chamo a função de gravar_arquivo com o parametro com o que eu quero salvar(saida) onde eu quero salvar(novo = saida.json)

    print("Endereço encontrado:", location.address)
    print("Coordenadas:", (location.latitude, location.longitude))
    print("Arquivo 'saida.json' gravado com sucesso!")
else:
    print("Não foi possível encontrar este endereço.")