contatos = {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "thiago@gmail.com", {}
)  # {"thiago@gmail.com": {"nome": "Thiago", "telefone": "3333-2221"}
print(resultado)