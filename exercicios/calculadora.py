#calculadora com o While

while True:
    numero_1 = input("Digite um numero: ")
    numero_2 = input("Digite outro numero: ")
    operador = input(" Escolha seu operdaor (+, -, /, *): ")

    numero_validos = None
    num_1 = 0
    num_2 = 0
    
    try:
        num_1 = float(numero_1)
        num_2 = float(numero_2)
        numero_validos = True
    except: 
        numero_validos = None


    if numero_validos is None:
       print('os numeros nao sao validos')
       continue

    operadores_permitidos = '+, -, /, *'
    if operador not in operadores_permitidos:
       print('operador invalido')
       continue
    
    if len(operador) > 1:
       print('voce digitou mais que um operador')
       continue

    print(' Realizando sua conta ')
    
    if operador == '+':
       print(num_1 + num_2)

    elif operador == '-':
       print(num_1 - num_2)
    
    elif operador == '/':
       print(num_1 / num_2)
    
    elif operador == '*':
       print(num_1 * num_2)
    
    else:
       print('voce fez algo de errado')
       

    sair = input("Quer sair? digite [s]im se nao digite qualquer outro botão ").lower().startswith("s")

    if sair is True:
     break