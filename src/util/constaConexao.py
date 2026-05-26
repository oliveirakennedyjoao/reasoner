from domain.Conexao import Conexao


def constaConexao(conexoes: list[Conexao], ordem: int):
    if conexoes is None or len(conexoes) == 0:
        return False
    else:
        for c in conexoes:
            if c.ordem == ordem:
                return True
        return False
