idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ").strip()
ano = int(input("Digite o ano: "))

erros = []

if idade <= 0:
    erros.append("Idade inválida.")

if curso == "":
    erros.append("Curso não pode ficar vazio.")

if ano < 1 or ano > 3:
    erros.append("Ano inválido.")

if len(erros) == 0:
    print("Cadastro válido!")
else:
    print("Cadastro inválido.")

    for erro in erros:
        print("-", erro)
