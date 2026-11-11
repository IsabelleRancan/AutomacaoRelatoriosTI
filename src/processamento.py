
import pandas as pd


COLUNAS_OBRIGATORIAS = [
    "ID",
    "Data de abertura",
    "Categoria",
    "Descrição",
    "Prioridade",
    "Status",
    "Tempo de atendimento (h)"
]

CATEGORIAS_VALIDAS = [
    "Hardware",
    "Sistemas",
    "Acessos"
]

PRIORIDADES_VALIDAS = [
    "Alta",
    "Média",
    "Baixa"
]

STATUS_VALIDOS = [
    "Concluído",
    "Em andamento",
    "Pendente"
]


def validar_dados(dados):

    erros = []

    # Verifica se todas as colunas existem
    colunas_ausentes = [
        coluna
        for coluna in COLUNAS_OBRIGATORIAS
        if coluna not in dados.columns
    ]

    if colunas_ausentes:
        erros.append(
            f"Colunas ausentes: {colunas_ausentes}"
        )
        return erros

    # Verifica campos obrigatórios
    campos_obrigatorios = [
        "ID",
        "Data de abertura",
        "Categoria",
        "Descrição",
        "Prioridade",
        "Status"
    ]

    for campo in campos_obrigatorios:
        if dados[campo].isna().any():
            erros.append(
                f"Existem valores vazios no campo: {campo}"
            )

    # Verifica IDs duplicados
    if dados["ID"].duplicated().any():
        erros.append("Existem IDs duplicados.")

    # Verifica categorias
    if not dados["Categoria"].isin(CATEGORIAS_VALIDAS).all():
        erros.append("Existem categorias inválidas.")

    # Verifica prioridades
    if not dados["Prioridade"].isin(PRIORIDADES_VALIDAS).all():
        erros.append("Existem prioridades inválidas.")

    # Verifica status
    if not dados["Status"].isin(STATUS_VALIDOS).all():
        erros.append("Existem status inválidos.")

    # Converte os tempos para valores numéricos
    tempos = pd.to_numeric(
        dados["Tempo de atendimento (h)"],
        errors="coerce"
    )

    # Verifica o tempo dos atendimentos concluídos
    concluidos = dados["Status"] == "Concluído"

    tempos_invalidos = (
        tempos[concluidos].isna()
        | (tempos[concluidos] <= 0)
    )

    if tempos_invalidos.any():
        erros.append(
            "Existem atendimentos concluídos sem tempo válido."
        )

    # Verifica tempos negativos
    if (tempos < 0).any():
        erros.append("Existem tempos de atendimento negativos.")

    return erros