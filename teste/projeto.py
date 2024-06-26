import os       
from cidades import *
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pausar():
    input("Pressione ENTER para continuar...")

def exibir_menu():
    print("===== MENU =====")
    print("1. Listar cidades")
    print("2. Adicionar cidade")
    print("3. Buscar cidade")
    print("4. Atualizar cidade")
    print("5. Remover cidade")
    print("0. Sair")
    
def processar_opcao(opcao):
    if opcao == "1":
        cidades = ler_cidades()
        for cidade in cidades:
            print("{cidade}")
            
    elif opcao == "2":
        nome_cidade = input("Digite o nome da cidade: ")
        adicionar_cidades(nome_cidade)
        print ("Cidade adicionada com sucesso!")
        
    elif opcao == "3":
        nome_cidade = input("Digite o nome da cidade: ")
        cidades_encotradas = buscar_cidade(nome_cidade)
        print("Cidades encontradas: ")
        for cidade in cidades_encotradas:
            print(cidade)
            
    elif opcao == "4": 
        nome_antigo = input("Digite o nome da cidade a ser atualizada: ") 
        nome_novo = input("Digite o novo nome da cidade: ")
        if atualizar_cidade(nome_antigo, nome_novo):
            print("Cidade atualizada com sucesso!")
        else:
            print("Cidade não encontrada!")
            
    elif opcao == "5":
        nome_cidade = input("Digite o nome da cidade a ser removida: ")
        if excluir_cidade(nome_cidade):
            print("Cidade removida com sucesso!")
        else:
            print("Cidade não encontrada!")
            
    elif opcao == "0":
        print("Saindo do sistema...")
        exit(0)
        
    else:
        print("Opção inválida!")
        
def executar_sistema():
    exibir_menu()
    opcao = input("Digite a opção desejada: ")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    executar_sistema()

executar_sistema()
