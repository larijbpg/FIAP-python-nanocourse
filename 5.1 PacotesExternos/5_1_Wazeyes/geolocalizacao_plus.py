from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "wazeyes")

endereco = input("Digite um endereço com numero e cidade: "
                 "(Exemplo: avenida paulista, 100 São Paulo): ")
resultado = str(geolocator.geocode(endereco)).split(",") 
# pesquisa a string recebida pelo usuario dentro do GoogleMaps e retorna em forma de string, com varios elementos separados por ",". 
# Por isso dividos a nossa string em elementos de uma lista a cada virgula encontrada na string

if resultado[0] != "None":
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[3])
    print("Cidade............: ", resultado[4])
    print("Região............: ", resultado[6])
