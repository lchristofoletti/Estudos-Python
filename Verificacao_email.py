# verificação de e-mail
nome = input("Qual o seu nome ? ")
email = input("Qual o seu email? ")

if len(nome) >= 3:
    if '@' and ".com" in email:
        print("Nome e E-mail cadastrados.")
    else:
        print("E-mail inválido")
else:
    print("Nome muito curto (minimo 3 caracteres)")
