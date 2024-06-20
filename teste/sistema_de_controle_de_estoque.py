estoque = []
def menu():
    print("Sistema de Controle de Estoque")
    print("1- Adicionar produto")
    print("2- Atualizar produto")
    print("3- Visualizar estoque")
    print("4. Sair")

    opcao = input("Escolha uma das opções acima: ")
    return opcao



def adicionar_produto():
    nome = input("Digite o nome do produto requisitado: ")
    preco = float(input("Digite o preço do produto solicitado: "))
    qntd = int(input("Digite a quantidade em estoque do produto: "))

    produto = {
        "nome": nome,
        "preço": preco,
        "quantidade": qntd
}   
    estoque.append(produto)
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("Digite o nome do produto a ser atualizado: ")
    encontrado = False


    for produto in estoque:
        if produto["nome"] == nome:
            preco = float(input("Digite o novo preço do produto solicitado: "))

            qntd = int(input("Digite a nova quantidade em estoque do produto: "))
            produto["preço"] = preco
            produto["quantidade"] = qntd


            encontrado =True
            print("Produto atualizado com sucesso!")
            break  
    if not encontrado:
        print("Produto não encontrado no nosso estoque")

def visualizar_estoque():
    if len(estoque) > 0:
        print("Estoque Atual: ")
        for produto in estoque:
            print(f"Nome:{produto['nome']}, Preço:{produto['preço']}, Quantidade:{produto['quantidade']}")
    else:
        print("O estoque no momento está vazio!")

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            atualizar_produto()
        elif opcao == '3':
            visualizar_estoque()
        elif opcao == '4':
            print("Saindo do sistema")
            break
    else:
        print("Opção inválida")
if __name__ == "__main__":
    main()

