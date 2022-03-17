nome = input("Qual o seu nome ? ")
idade = input("Qual sua idade ? ")
email = input("Qual o seu e-mail? ")


if nome.isalpha() and idade.isnumeric():
    p_arroba = email.find('@')
    dominio = email[p_arroba:]
    if p_arroba != -1 and '.' in dominio:
        print("\nBem vindo {}, seu cadastro foi concluido.\n".format(nome))
    else:
        print("E-mail invalido, favor inserir novamente")
else:
    print("Dados invalidos, insira novamente.")
