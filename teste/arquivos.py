def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
    print (conteudo)
    print (f"Lendo o arquivo: {nome_arquivo}")

def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "w")
    arquivo.write(conteudo)
    arquivo.close()

def adicionar_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(conteudo)
    arquivo.close()
    
def ler_linhas_arquivo(nome_arquivo):
    for linha in open(nome_arquivo, "r"):
        print(linha) 

ler_arquivo("cidades.txt")
escrever_arquivo("cidades.txt", "osasco\n")
ler_arquivo("cidades.txt")
adicionar_arquivo("cidades.txt", "são paulo\n")   
ler_arquivo("cidades.txt")


