# O seu modulo solicitará o nivel de acesso de uma pessoa que pode ser: ADM, USR ou GUEST e o genero dessa pessoa (fem ou masc)
# caso o nivel seja ADM, ele deverá exibir "Olá administrador" para os homens ou "Olá administradora" para as mulheres
# Se o nivel for USR, deverá exibir "Olá usuario" para os homens ou "Olá usuaria" para as mulheres
# Se o nivel for GUEST, a mensagem deverá exibir "Olá visitante.
# E se o nivel digitado for diferente de ADM, USR ou GUEST deverá eibir "Olá desconhecido(a)".

nivel_acesso = input('Qual seu nível de acesso? ADM, USR ou GUEST?').upper()
if nivel_acesso == 'ADM' or nivel_acesso == 'USR':
    genero = input('Qual seu genero? mulher ou homem?').upper()
    if nivel_acesso == 'ADM':
        if genero == 'HOMEM':
            print('Olá administrador')
        else:
            print('Olá administradora')
    else:
        if genero == 'MULHER':
            print('Ola usuaria')
        else:
            print('Olá usuario')
elif nivel_acesso == 'GUEST':
    print('Olá visitante')
else:
    print('Olá desconhecido(a)')







