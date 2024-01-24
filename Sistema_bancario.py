menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = """
| Descrição\t\t\t| Valor
------------------------------------------
"""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("------ DEPÓSITO ------")
        deposito = float(input("Digite o valor do depósito: R$"))
        
        if deposito > 0:
            saldo += deposito
            print("Operação realizada com sucesso!")
            linha = f"| Depósito \t\t\t| R$ {deposito}"
            extrato += linha + "\n"
        else:
            print("Só é possível realizar depósitos com o valor maior que zero")
        
    elif opcao == "s":
        print("------ SAQUE ------")
        if numero_saque < LIMITE_SAQUE:
            saque = float(input("Digite o valor que deseja sacar: R$"))
            
            if 0 < saque <= saldo and saque <= 500:
                saldo -= saque
                numero_saque += 1
                print("Operação realizada com sucesso!")
                linha = f"| Saque \t\t\t| R$ {saque}"
                extrato += linha + "\n"
            else:
                print("Operação não pode ser realizada, verifique seu saldo ou seu limite de saque")
        else:   
            print("Você já fez 3 saques hoje, entre em contato com o banco")
        
    elif opcao == "e":
        print(extrato)
        print("------------------------------------------")
        print(f"Total \t\t\t\t R${saldo}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione a opção desejada novamente...")
