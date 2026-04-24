# main.py

from contactos import (
    adicionar_contacto,
    listar_contactos,
    pesquisar_por_nome,
    pesquisar_por_telefone,
    remover_contacto,
    guardar_contactos,
    carregar_contactos
)

from utils import (
    validar_nome,
    validar_telefone,
    validar_email
)


# Nome do ficheiro onde os contactos serão guardados
NOME_FICHEIRO = "contactos.json"


# Função para mostrar o menu principal
def exibir_menu():
    print("\n===== GESTOR DE CONTACTOS =====")
    print("1. Adicionar contacto")
    print("2. Listar todos os contactos")
    print("3. Pesquisar contacto por nome")
    print("4. Pesquisar contacto por telefone")
    print("5. Remover contacto")
    print("6. Guardar contactos")
    print("7. Carregar contactos")
    print("0. Sair")

    return input("Escolhe uma opção: ")


# Função para mostrar os resultados de uma pesquisa
def mostrar_resultados(resultados):
    if len(resultados) == 0:
        print("Não foram encontrados contactos.")
    else:
        print("\n===== RESULTADOS DA PESQUISA =====")

        for contacto in resultados:
            print("--------------------")
            print("Nome:", contacto["nome"])
            print("Telefone:", contacto["telefone"])
            print("Email:", contacto["email"])


# Lista principal de contactos — carregada automaticamente do ficheiro
lista_contactos = carregar_contactos(NOME_FICHEIRO)


# Ciclo principal do programa
while True:
    opcao = exibir_menu()

    if opcao == "1":
        print("\nAdicionar contacto")

        nome = input("Nome: ")

        if not validar_nome(nome):
            print("Erro: o nome não pode estar vazio.")
            continue

        telefone = input("Telefone: ")

        if not validar_telefone(telefone):
            print("Erro: o telefone deve ter 9 dígitos e conter apenas números.")
            continue

        email = input("Email: ")

        if not validar_email(email):
            print("Erro: email inválido.")
            continue

        if adicionar_contacto(lista_contactos, nome, telefone, email):
            print("Contacto adicionado com sucesso.")
        else:
            print("Erro: já existe um contacto com esse telefone.")

    elif opcao == "2":
        listar_contactos(lista_contactos)

    elif opcao == "3":
        nome = input("Introduz o nome a pesquisar: ")

        resultados = pesquisar_por_nome(lista_contactos, nome)
        mostrar_resultados(resultados)

    elif opcao == "4":
        telefone = input("Introduz o telefone a pesquisar: ")

        resultados = pesquisar_por_telefone(lista_contactos, telefone)
        mostrar_resultados(resultados)

    elif opcao == "5":
        telefone = input("Introduz o telefone do contacto a remover: ")

        removido = remover_contacto(lista_contactos, telefone)

        if removido:
            print("Contacto removido com sucesso.")
        else:
            print("Contacto não encontrado.")

    elif opcao == "6":
        guardar_contactos(lista_contactos, NOME_FICHEIRO)
        print("Contactos guardados com sucesso.")

    elif opcao == "7":
        lista_contactos = carregar_contactos(NOME_FICHEIRO)
        print("Contactos carregados com sucesso.")

    elif opcao == "0":
        guardar_contactos(lista_contactos, NOME_FICHEIRO)
        print("Contactos guardados. Programa terminado.")
        break

    else:
        print("Opção inválida. Tenta novamente.")


