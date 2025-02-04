contato = {"nome": "Thiago", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Thiago"
print(contato)  # {'nome': 'Thiago', 'telefone': '3333-2221'}

contato.setdefault("idade", 18)  # 18
print(contato)  # {'nome': 'Thiago', 'telefone': '3333-2221', 'idade': 18}