def validar_dados(nome, email):
    if not nome or not email:
        return False, "Todos os campos devem estar preenchidos"
    if "@" not in email:
        return False, "Email inválido"
    return True, "Dados válidos"