Menu = """
[1] Depositar
[2] Extrato
[3] Sacar
[4] sair 

=> """

Saldo = 2500
Limite = 500 
Extrato = ""
Numero_saques = 0
Limite_saques = 3

while True:
    opcao = input(Menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            Saldo += valor
            Extrato += f"depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou, valor inválido.")



    elif opcao == "2":
        print("\n ========== Extrato: ==========")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\n"f" Saldo: R$ {Saldo:.2f}\n")
        print("==============================")


    elif opcao == "3":
        valor = float(input("Informe o valor do Saque:"))

        excedeu_saldo = valor > Saldo
        excedeu_limite = valor > Limite
        excedeu_saques = Numero_saques >= Limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Erro na operação, limite excedido")

        elif excedeu_saques:
            print("Numero máximo de saque excedido")

        elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}"
            Numero_saques += 1

        else:
            print("Operação falhou, valor inválido.")



    elif opcao == "4":
        break


    
    else:
        print("Operação inválida. por favor selecione novamente.")