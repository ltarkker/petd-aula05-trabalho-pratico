# contactos.py

import json


# Função para adicionar um novo contacto à lista
def adicionar_contacto(lista_contactos, nome, telefone, email):
    for contacto in lista_contactos:
        if contacto["telefone"] == telefone:
            return False

    novo_contacto = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    lista_contactos.append(novo_contacto)
    return True


# Função para listar todos os contactos
def listar_contactos(lista_contactos):
    if len(lista_contactos) == 0:
        print("Não existem contactos registados.")
    else:
        print("\n===== LISTA DE CONTACTOS =====")

        for contacto in lista_contactos:
            print("--------------------")
            print("Nome:", contacto["nome"])
            print("Telefone:", contacto["telefone"])
            print("Email:", contacto["email"])


# Função para pesquisar contactos pelo nome
def pesquisar_por_nome(lista_contactos, nome):
    resultados = []

    for contacto in lista_contactos:
        if nome.lower() in contacto["nome"].lower():
            resultados.append(contacto)

    return resultados


# Função para pesquisar contactos pelo telefone
def pesquisar_por_telefone(lista_contactos, telefone):
    resultados = []

    for contacto in lista_contactos:
        if telefone in contacto["telefone"]:
            resultados.append(contacto)

    return resultados


# Função para remover um contacto pelo telefone
def remover_contacto(lista_contactos, telefone):
    for contacto in lista_contactos:
        if contacto["telefone"] == telefone:
            lista_contactos.remove(contacto)
            return True

    return False


# Função para guardar os contactos num ficheiro JSON
def guardar_contactos(lista_contactos, nome_ficheiro):
    with open(nome_ficheiro, "w", encoding="utf-8") as ficheiro:
        json.dump(lista_contactos, ficheiro, ensure_ascii=False, indent=4)


# Função para carregar os contactos a partir de um ficheiro JSON
def carregar_contactos(nome_ficheiro):
    try:
        with open(nome_ficheiro, "r", encoding="utf-8") as ficheiro:
            contactos = json.load(ficheiro)
            return contactos

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []