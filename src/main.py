from pathlib import Path
import pandas as pd
from datetime import datetime

from automacao import abrir_arquivo
from processamento import validar_dados


def main():

    print("\n=== AUTOMAÇÃO DE ATENDIMENTOS DE TI ===")

    caminho_projeto = Path(__file__).resolve().parents[1]
    arquivo = caminho_projeto / "dados" / "atendimentos.xlsx"

    # Etapa 1: verifica se a planilha existe
    print("\nLocalizando planilha...")

    if not arquivo.exists():
        print("Erro: planilha não encontrada.")
        return

    print("Planilha localizada!")

    # Etapa 2: leitura dos dados
    print("\nLendo planilha...")

    try:
        dados = pd.read_excel(arquivo, sheet_name="ATENDIMENTOS")

    except PermissionError:
        print("\nErro: não foi possível acessar a planilha.")
        print("Feche o arquivo atendimentos.xlsx no Excel e tente novamente.")
        return

    print(f"{len(dados)} atendimentos encontrados.")

    # Etapa 3: validação
    print("\nValidando informações...")
    erros = validar_dados(dados)

    if erros:
        print("\nForam encontrados problemas:")

        for erro in erros:
            print(f"- {erro}")

        print("\nProcessamento interrompido.")
        return

    print("Dados validados com sucesso!")

    data_geracao = datetime.now()

    print("\nGerando relatório...")

    pasta_relatorios = caminho_projeto / "relatorios"
    pasta_relatorios.mkdir(exist_ok=True)

    nome_arquivo = (
    f"relatorio_atendimentos_"
    f"{data_geracao.strftime('%Y%m%d_%H%M%S')}.xlsx"
)

    caminho_relatorio = pasta_relatorios / nome_arquivo

    resumo = (
        dados["Status"]
        .value_counts()
        .rename_axis("Status")
        .reset_index(name="Quantidade")
    )

    # Calcula o intervalo de dados do resumo
    ultima_linha = len(resumo) + 1

    intervalo_grafico = f"A1:B{ultima_linha}"

    resumo = resumo.astype(object)

    resumo.loc[len(resumo)] = [None, None]

    resumo.loc[len(resumo)] = [
        "Data de geração",
        data_geracao.strftime("%d-%m-%Y %H:%M")
    ]

    with pd.ExcelWriter(caminho_relatorio, engine="openpyxl") as writer:
        resumo.to_excel(writer, sheet_name="Resumo", index=False)
        dados.to_excel(writer, sheet_name="Atendimentos", index=False)

    print("Relatório gerado com sucesso!")

    # Etapa 4: interação com o Windows
    print("\nAbrindo relatório no Excel...")

    if not abrir_arquivo(caminho_relatorio, intervalo_grafico):
        print("Não foi possível abrir e formatar o relatório.")
        return
    
    print("\n=== PROCESSAMENTO CONCLUÍDO ===")

if __name__ == "__main__":
    main()