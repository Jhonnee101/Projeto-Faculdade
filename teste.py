import json

def carregar_comandas():
    try:
        with open("comandas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvar_comandas(comandas):
    with open("comandas.json", "w") as file:
        json.dump(comandas, file)
def nova_comanda(comandas):
    num_mesa = input("Digite o número da nova comanda: ")
    num_comanda = "Mesa " + num_mesa
    comandas[num_comanda] = []
    print(f"{num_comanda} criada com sucesso.")

def adicionar_produtos(comandas):
    num_comanda = input("Digite o número da comanda: ")
    if num_comanda in comandas:
        while True:
            print("-----------------------------")
            print("Deseja adicionar algum pedido?")
            print("[1] - Sim.")
            print("[2] - Não.")
            print("-----------------------------")
            escolha = input("Escolha uma opção: ")
            if escolha == "1":
                produto = input("Digite o produto a ser adicionado: ")
                preco = float(input("Digite o preço: "))
                quantidade = int(input("Digite a quantidade: "))
                valor = quantidade * preco
                comandas[num_comanda].append({"Produto": produto, "Preço": preco, "Quantidade": quantidade, "Valor": valor})
            elif escolha == "2":
                print("Produtos salvos com sucesso")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
    else:
        print("Comanda não encontrada.")

def calcular_total(comanda):
    return sum(item["Valor"] for item in comanda)

def fechar_comanda(comandas):
    num_comanda = input("Digite o número da comanda a ser fechada: ")
    if num_comanda in comandas:
        total = calcular_total(comandas[num_comanda])
        print("Calculando a soma dos valores dos produtos...")
        print(f"Total a pagar: R$ {total} ")
        pagamento = float(input("Qual o valor do pagamento? "))
        troco = pagamento - total
        print(f"O seu troco será R${troco:.2f}, Obrigado pela preferencia")
        del comandas[num_comanda]
        print("Comanda fechada.")
    else:
        print("Comanda não encontrada.")

def menu():
    comandas = carregar_comandas()

    while True:
        print("\n--- Menu ---")
        print("[1] - Nova Comanda")
        print("[2] - Adicionar Produtos")
        print("[3] - Fechar Comanda")
        print("[4] - Salvar Comandas")
        print("[5] - Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_comanda(comandas)
        elif opcao == "2":
            adicionar_produtos(comandas)
        elif opcao == "3":
            fechar_comanda(comandas)
        elif opcao == "4":
            salvar_comandas(comandas)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

menu()
