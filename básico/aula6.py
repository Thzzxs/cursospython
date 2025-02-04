nome = "Thiago"
print(nome[2])
print(nome[-4])
print("i" in nome)
print(10* "-")
print("tt" in nome)
print("tato" not in nome)

nome = input("Digite seu nome: ")
encontrar= input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} esta em {nome}")
else:
    print(f"{encontrar} não esta em {nome}")
