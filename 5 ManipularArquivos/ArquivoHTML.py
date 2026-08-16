with open('pagina.html', 'w') as pagina:
    pagina.write('<body> <h1> Este é um teste para a página WEB </h1>')
    pagina.write('<br><h2> Abaixo seguem alguns nomes importantes para o projeto: </h2>')
    pagina.write('<h3>')
    nome = ''

    while nome != 'SAIR':
        nome = input('Digite um nome ou SAIR: ').upper()
        if nome != 'SAIR':
            pagina.write('<br>' + nome)
    pagina.write('</h3></body') # após o laço while encerrar, fechamos a formatação <h3> e <body>