# Esse programinha foi feito para treinar as habilidades de condicional
# Desafio:#
#  Cálculo de Bônus
# Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:
# A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
# Caso contrário o valor de bônus do funcionário é 0.
# Print o bônus dos 3 funcionários
# Se o usuario não digitar nada, printar uma msg para que seja feito a inserção corretamente

# Exercicio basico e de facil entendimento

funcionario_1 = input("Quanto o Funcionario 1 vendeu? \n")
funcionario_2 = input("Quanto o Funcionario 2 vendeu? \n")
funcionario_3 = input("Quanto o Funcionario 3 vendeu? \n")

meta = 1000
meta2 = 2000
bonus1 = 0.10
bonus2 = 0.15

if funcionario_1 == '' or funcionario_2 == '' or funcionario_3 == '':
    print("Digite os valores de vendas corretamente!!!")
else:
    if int(funcionario_1) >= meta:
        if int(funcionario_1) < meta2:
            print("\nFuncionario 1 bateu a meta, recebeu o bônus de: R$ {}\n".format(
                int(funcionario_1)*bonus1))
    if int(funcionario_1) < meta:
        bonus1 = 0
        print("Funcionario 1 não bateu a meta, recebeu o bônus de: R$ {}\n".format(bonus1))
    if int(funcionario_1) >= meta2:
        print("Funcionario 1 bateu a meta maior, recebeu o bônus de: R$ {}\n".format(
            int(funcionario_1)*bonus2))

    if int(funcionario_2) >= meta:
        if int(funcionario_2) < meta2:
            print("Funcionario 2 bateu a meta, recebeu o bônus de: R$ {}\n".format(
                int(funcionario_2)*bonus1))
    if int(funcionario_2) < meta:
        bonus1 = 0
        print("Funcionario 2 não bateu a meta, recebeu o bônus de: R$ {}\n".format(bonus1))
    if int(funcionario_2) >= meta2:
        print("Funcionario 2 bateu a meta maior, recebeu o bônus de: R$ {}\n".format(
            int(funcionario_2)*bonus2))

    if int(funcionario_3) >= meta:
        if int(funcionario_3) < meta2:
            print("Funcionario 3 bateu a meta, recebeu o bônus de: R$ {}\n".format(
                int(funcionario_3)*bonus1))
    if int(funcionario_3) < meta:
        bonus1 = 0
        print("Funcionario 3 não bateu a meta, recebeu o bônus de: R$ {}\n".format(bonus1))
    if int(funcionario_3) >= meta2:
        print("Funcionario 3 bateu a meta maior, recebeu o bônus de: R$ {}\n".format(
            int(funcionario_3)*bonus2))
