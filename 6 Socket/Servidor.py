from socket import *

servidor = "127.0.0.1" # poderiamos usar "localhost", para identificar que o servidor é a propria maquina que esta executando o codigo
porta = 43210 #(numero inteiro entre 0 e 65535)

obj_socket = socket(AF_INET, SOCK_STREAM) 
    # a função socket() existe 2 parametro: 
        # 1°parametro define a familia responsavel por identificar os pacotes
            #AF_INET, identificação do emissor/receptor dos pacotes via DNS/IP
        # 2°parametro refere-se ao transporte desse pacote, que pode ser SOCK_STREAM(protocolo TCP - mais confiável) ou SOCK_DGRAM(protocolo UDP)
obj_socket.bind((servidor, porta)) # associação no nosso objeto socket com o nosso servidor e porta
obj_socket.listen(2) # listen define o maximo de clientes que o nosso servidor vai atender simultaneamente, que será 2
print("Aguardando cliente...")

while True: # laço infinito
    con, cliente = obj_socket.accept() 
    # aguardamos a chamada do cliente(por meio da função accept()) e assim que tiver, 
    # receberá uma tupla que será direcionada a identificação do cliente para a variavel "cliente"
    # e a identificação da conexão para a variavel "con"
    print("Conectador com: ", cliente) # exibi a identificação do cliente
    while True: # segundo laço
        msg_recebida = str(con.recv(1024)) #aguardamos uma solicitação que pode ser transmitida em pacotes de 1024bytes
        print("Recebemos: ", msg_recebida) #exibimos a msg recebida
        msg_enviada = b'Olah cliente' #geramos uma msg para enviar no formato de "bytes" (por isso a msg começa com 'b')
        con.send(msg_enviada) # a msg é enviada pelo metodo send()
        break 
    con.close()