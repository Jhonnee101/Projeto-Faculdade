from openpyxl import Workbook, load_workbook

def criar_planilha():
    workbook = Workbook()
    planilha = workbook.active
    planilha.title = "Comandas"
    planilha.append(["Número da Comanda", "Produtos"])

    return workbook

def nova_comanda(planilha):
    num_comanda = input("Digite o número da nova comanda: ")
    planilha.create_sheet(title=num_comanda)
    print(f"Comanda {num_comanda} criada com sucesso.")

def adicionar_produtos(planilha):
    num_comanda = input("Digite o número da comanda: ")
    if num_comanda in planilha.sheetnames:
        produtos = input("Digite os produtos a serem adicionados (separados por vírgula): ")
        planilha[num_comanda].append([produtos])
        print("Produtos adicionados à comanda.")
    else:
        print("Comanda não encontrada.")

def fechar_comanda(planilha):
    num_comanda = input("Digite o número da comanda a ser fechada: ")
    if num_comanda in planilha.sheetnames:
        produtos = planilha[num_comanda].cell(row=2, column=1).value
        print(f"Comanda {num_comanda} contém os seguintes produtos: {produtos}")
        planilha.remove(planilha[num_comanda])
        print("Comanda fechada.")
    else:
        print("Comanda não encontrada.")

def salvar_planilha(workbook):
    nome_arquivo = "comandas.xlsx"
    workbook.save(nome_arquivo)
    print(f"Planilha salva como '{nome_arquivo}'.")

def menu():
    workbook = criar_planilha()

    while True:
        print("\n--- Menu ---")
        print("1. Nova Comanda")
        print("2. Adicionar Produtos")
        print("3. Fechar Comanda")
        print("4. Salvar Planilha")
        print("5. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_comanda(workbook)
        elif opcao == "2":
            adicionar_produtos(workbook)
        elif opcao == "3":
            fechar_comanda(workbook)
        elif opcao == "4":
            salvar_planilha(workbook)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()