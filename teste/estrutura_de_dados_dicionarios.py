# Manipulando dicionários

cliente = {
    "nome": "Paulo", 
    "cidade": "São Paulo",
    "ano_nasc": 2005,
    "ativo": False
}
print(cliente["nome"])

cliente["ano_nasc"] = 2000
print(cliente)

del cliente["cidade"]
print(cliente)

if "ano_nasc" in cliente:
    print(f"O cliente nasceu em: {cliente['ano_nasc']}")
else:
    print(f"Não existe a chave ano_nascimento")

print (f"Lista de valores: ")
for valor in cliente.values():
    print(valor)

print(f"Lista de chaves: ")
for chave, valor in cliente.items():
    print(chave)