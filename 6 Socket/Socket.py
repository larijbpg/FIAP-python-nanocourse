import socket 

resp = "S"
while resp == "S": # laço para que enquanto digite a letra "s", o codigo continue perguntando uma url e exibindo seu IP. Só será encerrado caso o usuario digite algo diferente de "s"
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)

    resp = input("Digite <S> para continuar: ").upper()