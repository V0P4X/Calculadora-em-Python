def calculadora():
    print("=== CALCULADORA PYTHON ===")

    while True:
        print("\nEscolha uma operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")

        opcao = input("Opção: ")

        if opcao == "5":
            print("Encerrando...")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == "1":
            resultado = n1 + n2
            operacao = "+"
        elif opcao == "2":
            resultado = n1 - n2
            operacao = "-"
        elif opcao == "3":
            resultado = n1 * n2
            operacao = "*"
        elif opcao == "4":
            if n2 == 0:
                print("Não é possível dividir por zero!")
                continue
            resultado = n1 / n2
            operacao = "/"

        print(f"\nResultado: {n1} {operacao} {n2} = {resultado}")

calculadora()
