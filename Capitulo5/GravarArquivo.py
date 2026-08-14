with open('teste.txt', 'w') as arquivo:
    arquivo.write('Nunca foi tão fácil criar um arquivo.')

with open('teste.txt', 'a') as arquivo: # mudei de 'w' para 'a' para adicionar a segunda frase e não sobrepor apenas.
    arquivo.write(' Continuação do texto.')