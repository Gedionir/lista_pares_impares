num_par = [[]]
num_impar = [[]]
valor = 0
for c in range(1, 10):
    valor = int(input("Digite um valor:"))
    if valor % 2 == 0:
        num_par[0].append(valor)
    else:
        num_impar[0].append(valor)
print("-="*30)
print(f"Todos os valores pares: {num_par}")
print(f"Todos os valores ímpares: {num_impar}")
