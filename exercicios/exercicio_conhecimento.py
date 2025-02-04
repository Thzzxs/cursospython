nome = input ("Digite seu nome: ")
idade = input ("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}" )
    print(f"Seu nome invertido é  {nome[::-1]}" )

    if " " in nome:
        print("Seu nome contem espaço ")
    else:
         print("Seu nome nao contem espaço ")
     
    print(f"Seu nome tem {len(nome)} letras" )
    print(f"a primeira letra do seu nome é {nome[0]}" )
    print(f"a ultima letra do seu nome é {nome[-1]}" )
else:
    print("Desculpe, voce deixou vazio esse campo, faça denovo" )

