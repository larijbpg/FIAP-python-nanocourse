from socket import *

servidor = "127.0.0.1"
porta = 43210

msg = bytes(input("Digite algo: "), "utf-8") # socket só transmite dados em bytes
obj_socket = socket(AF_INET, SOCK_STREAM)
    # obj_socket => como se fosse um celular, crio meu celular, walkie-talk, telefone
    # o Python reserva um espaço de memoria no meu computador e prepara o "aparelho" virtual que é capaz de falar com a rede
    # os parâmetros dizem que tipo de ligação quero fazer
        # AF_INET => cte que define o protocolo IPv4 - vou me conectar usando um endereço de IP comum
        # SOCK_STREAM => quero uma ligação confiável, do tipo TCP - chegue na ordem certa e sem perdas
    #RESUMINDO: Python, crie um aparelho de conexão(obj_socket) preparado para usar endereços de IP padrão(AF_INET) e que converse de forma confiavel e sem perdas de dados (SOCK_STREAM)
obj_socket.connect((servidor, porta)) 
#connect() => pega o meu socket e estabelece uma linha direta com o computador/servidor de destino.
obj_socket.send(msg)
resposta = obj_socket.recv(1024) # o meu aparelho vai receber o dado enviado pelo servidor, limitando o tamanho para 1024 bytes
print("Recebemos: ", resposta) # exibe a resposta
obj_socket.close() # fecha a conexão