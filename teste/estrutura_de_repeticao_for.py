numero = int(input("Digite um número: "))

print(f"Tabuada do {numero}: ")

resultado = 1 * numero
print(f"{numero} X 1 = {resultado}")

for i in range(1, 11):
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")