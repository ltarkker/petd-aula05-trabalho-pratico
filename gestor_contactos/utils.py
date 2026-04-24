# utils.py

import re


# Função para validar se o nome não está vazio
def validar_nome(nome):
    if not isinstance(nome, str):
        return False
    if nome.strip() == "":
        return False
    return True

# Função para validar telefone
def validar_telefone(telefone):
    # Verifica se tem apenas números
    if not telefone.isdigit():
        return False

    # Verifica se tem 9 digitos
    if len(telefone) != 9:
        return False

    return True

# Função para validar email
def validar_email(email):
    if not isinstance(email, str):
        return False

    # Formato: <local>@<domínio>.<tld> — nenhuma parte pode ser vazia
    padrao = r"^[^\s@]+@[^\s@.]+\.[^\s@.]+$"
    return re.match(padrao, email) is not None

