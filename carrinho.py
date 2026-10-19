def exibir_menu():
    print("\n--- SISTEMA DE CARRINHO DE COMPRAS ---")
    print("1. Adicionar produto")
    print("2. Ver carrinho")
    print("3. Remover produto")
    print("4. Finalizar compra")
    print("5. Sair")


def carrinho():
    itens = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Digite o nome do produto: ")
            itens.append(produto)
            print(f"Produto '{produto}' adicionado ao carrinho.")
        elif opcao == "2":
            if itens:
                print("Produtos no carrinho:")
                for i, item in enumerate(itens, 1):
                    print(f"{i}. {item}")
            else:
                print("Seu carrinho está vazio.")
        elif opcao == "3":
            if itens:
                produto = input("Digite o nome do produto a remover: ")
                if produto in itens:
                    itens.remove(produto)
                    print(f"Produto '{produto}' removido do carrinho.")
                else:
                    print("Produto não encontrado no carrinho.")
            else:
                print("Seu carrinho está vazio.")
        elif opcao == "4":
            if itens:
                print("Compra finalizada com sucesso!")
                print("Itens comprados:")
                for item in itens:
                    print(f"- {item}")
                break
            else:
                print("Seu carrinho está vazio. Adicione produtos antes de finalizar.")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


carrinho()