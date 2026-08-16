# lista vazia 
lista_vazia = []


# lista preenchida estaticamente
lista_estatica = ['xpto', True]


# lista preenchida dinamicamente
lista_dinamica = [input('Digite o usuário: '), bool(int(input('Está logado? ')))]
print(lista_dinamica)

    # Guardar como booleano (True/False) é fundamental para que, mais para frente no código, você possa fazer decisões automáticas com if
        # nesse caso, como quero uma resposta sim ou não, vou converter o dado para booleano.
        # entretanto, nao pode fazer a conversão diretamente de string para bool, então converto para inteiro e depois para booleano.
        # o valor será falso apenas se o valor retornado for 0. Qualquer outro valor, será considerado True.

# # Exemplo de como usaríamos essa lista depois:
    # if lista_dinamica[1] == True:
    #     print("Acesso liberado aos laudos!")
    # else:
    #     print("Acesso negado: Faça o login primeiro.")
    