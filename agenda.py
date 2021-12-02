""" 
	Formato de escrita na agenda:

	Nome/Telefone/Endereco
	... /  ...   / (Rua)

"""

# Carregando o arquivo para um dicionario
agenda = open("arquivo.txt", "r")
data = {}

for line in agenda:
	nome, telefone, endereco = line.split("/")
	endereco = endereco[0:-1]
	data[nome] = [telefone, endereco]

agenda.close()


def inserir():
	nome = input("Nome: ")
	if nome in data:
		print("Nome ja existente na agenda.")
		return

	telefone = input("Numero: ")
	endereco = input("Endereco: ")

	data[nome] = [telefone, endereco]


def busca(nome):
	acontecimentos = {}

	for name in data:
		if nome == name:
			acontecimentos.clear()
			acontecimentos[name] = data[name]
			return acontecimentos
		elif nome.upper() in name.upper():
			acontecimentos[name] = data[name]

	return acontecimentos


def remove():
	nome = input("Nome da pessoa a ser removida: ")

	ocorrencias = busca(nome)
	if not ocorrencias:
		print("Nenhuma ocorrencia deste nome")
	elif len(ocorrencias) > 1:
		for ocorrencia in ocorrencias:
			print(ocorrencia, ocorrencias[ocorrencia][0], ocorrencias[ocorrencia][1])
		print("Foi vista mais de uma ocorrencia para este nome, seja mais especifico(a)")
	else:
		data.pop(nome)



def edita():
	nome = input("Nome da pessoa a ser editada: ")

	ocorrencias = busca(nome)
	if not ocorrencias:
		print("Nenhuma ocorrencia deste nome")
	elif len(ocorrencias) > 1:
		for ocorrencia in ocorrencias:
			print(ocorrencia, ocorrencias[ocorrencia][0], ocorrencias[ocorrencia][1])
		print("Foi vista mais de uma ocorrencia para este nome, seja mais especifico(a)")
	else:
		print(ocorrencias)
		telefone = input("Telefone: ")
		endereco = input("Endereco: ")
		data[nome] = [telefone, endereco]


eventos = ["Inserir", "Buscar", "Remover", "Editar"]
c = ""
while c != "end":
	evento = input("Escolha o passo: (Inserir, Buscar, Remover, Editar) ")
	if evento not in eventos:
		continue

	if evento == eventos[0]:
		inserir()
	elif evento == eventos[1]:
		nome = input("Nome a ser buscado: ")
		buscado = busca(nome)
		print(buscado)
	elif evento == eventos[2]:
		remove()
	else:
		edita()

	c = input("Novamente? (Digite 'end' para terminar) ")



agenda = open("arquivo.txt", "w")
for name in data:
	agenda.writelines(f"{name}/{data[name][0]}/{data[name][1]}\n")

agenda.close()
