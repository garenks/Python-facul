usuarios = {"ana", "maria", "ana"}
usuarios.add("felipe")
print (usuarios)

usuario_digitado = input("Digite seu usuário: ")
if usuario_digitado in usuarios:
    print(f"Usuário cadastrado com sucesso!")
else:
    print(f"Usuário não cadastrado!")

novos_usuarios = {"felipe", "pedro", "marcos"}
print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios)
print(f"união: {todos_usuarios}")

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"interseção: {usuarios_comuns}")

usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"diferença: {usuarios_diferentes}")