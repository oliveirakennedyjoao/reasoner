from domain.Conexao import Conexao


def ordenaConexao(conexoes: list[Conexao]) -> list[Conexao]:
    return sorted(conexoes, key=lambda c: c.ordem)
