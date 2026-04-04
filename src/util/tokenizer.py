

def tokenize(expr: str):
    tokens = []
    i = 0
    n = len(expr)

    while i < n:
        char = expr[i]

        # 1. Ignorar espaços
        if char.isspace():
            i += 1
            continue

        # 2. Operador composto |=
        if expr[i:i+2] == "|=":
            tokens.append("|=")
            i += 2
            continue

        # 3. Parênteses e operadores simples
        if char in {"(", ")", "⊑", "⊓", "⊔", "¬", "∃", "∀", "."}:
            tokens.append(char)
            i += 1
            continue

        # 4. Identificadores + possível função (ex: OL(a))
        if char.isalpha():
            start = i

            # lê nome (ex: OL, CO, h)
            while i < n and expr[i].isalnum():
                i += 1

            nome = expr[start:i]

            # se vier "(" depois → função
            if i < n and expr[i] == "(":
                count = 0
                func_start = start

                while i < n:
                    if expr[i] == "(":
                        count += 1
                    elif expr[i] == ")":
                        count -= 1
                        if count == 0:
                            i += 1
                            break
                    i += 1

                tokens.append(expr[func_start:i])
            else:
                tokens.append(nome)

            continue

        # 5. Qualquer coisa inesperada
        raise ValueError(f"Caractere inesperado: {char}")

    return tokens
