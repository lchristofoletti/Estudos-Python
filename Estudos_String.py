cpf = input("Qual os numeros do seu CPF ?")
# Comando Strip usado para retirar espaços vazios, tanto no inicio quanto no final
cpf = cpf.strip()
# COmando replace utilizado para substituir caracteres
cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")
# comando len utilizado para sinalizar que está se referindo a quantidade de caracter
# comando isnumeric para identificação que o caracter é numero
if len(cpf) == 11 and cpf.isnumeric:
    print("Seu CPF é : {}".format(cpf))
else:
    print("Favor inserir os 11 numeros do seu CPF (SOMENTE NUMEROS)")
