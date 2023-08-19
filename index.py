comandas = {}

def nova_comanda():
    num_comanda = input("Digite o número da nova comanda: ")
    comandas[num_comanda] = []
    print(f"Comanda {num_comanda} criada com sucesso.")

def adicionar_produtos():
    num_comanda = input("Digite o número da comanda: ")
    if num_comanda in comandas:
        produtos = input("Digite os produtos a serem adicionados (separados por vírgula): ")
        comandas[num_comanda].extend(produtos.split(","))
        print("Produtos adicionados à comanda.")
    else:
        print("Comanda não encontrada.")

def fechar_comanda():
    num_comanda = input("Digite o número da comanda a ser fechada: ")
    if num_comanda in comandas:
        produtos = comandas[num_comanda]
        total = len(produtos)
        print(f"Comanda {num_comanda} contém {total} produtos: {', '.join(produtos)}")
        del comandas[num_comanda]
        print("Comanda fechada.")
    else:
        print("Comanda não encontrada.")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Nova Comanda")
        print("2. Adicionar Produtos")
        print("3. Fechar Comanda")
        print("4. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_comanda()
        elif opcao == "2":
            adicionar_produtos()
        elif opcao == "3":
            fechar_comanda()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()