#Ana Clarisse e Hugo Otávio
#14. Crie um dicionário que armazene o nome e o telefone de 5 contatos. Escreva um programa que permita ao usuário buscar o telefone de um contato pelo nome.

contatos= {"toinha": "Número: (85)91111-1111", "hugo": "Número: (85)92222-1111", "pamela": "Número: (85)93333-1111", "tio paulo": "Número: (85)95555-1111", "felipe" : "Número: (85)94444-1111"}
print("Contatos: \n toinha \n hugo \n pamela \n tio paulo \nfelipe")
nome = input("Nome: ").lower()

if nome in contatos:
    contatos = contatos[nome]
    print(contatos)
else:
    print("Não encontrado")