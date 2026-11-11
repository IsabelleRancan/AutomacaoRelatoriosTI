from pathlib import Path
from processamento import validar_dados
import pandas as pd

# Localização da planilha
caminho_projeto = Path(__file__).resolve().parents[1]
caminho_arquivo = caminho_projeto / "dados" / "atendimentos.xlsx"

# Verifica se o arquivo existe
if not caminho_arquivo.exists():
    print("Arquivo não encontrado!")
else:
    # Lê a planilha
    dados = pd.read_excel(caminho_arquivo, sheet_name="ATENDIMENTOS")

    # Exibe informações da base
    print("\n--- ESTRUTURA DA PLANILHA ---")
    print(f"Quantidade de registros: {dados.shape[0]}")
    print(f"Quantidade de colunas: {dados.shape[1]}")

    print("\n--- NOMES DAS COLUNAS ---")
    print(dados.columns.tolist())

    print("\n--- PRIMEIROS REGISTROS ---")
    print(dados.head())

    print("\n--- TIPOS DE DADOS ---")
    print(dados.dtypes)

    print("\n--- VALORES AUSENTES ---")
    print(dados.isnull().sum())

    print("\n--- ATENDIMENTOS POR STATUS ---")
print(dados["Status"].value_counts())

print("\n--- TEMPO DE ATENDIMENTO POR STATUS ---")
print(
    pd.crosstab(
        dados["Status"],
        dados["Tempo de atendimento (h)"].isna(),
        margins=True
    )
)

print("\n--- IDS DUPLICADOS ---")
print(dados[dados["ID"].duplicated(keep=False)])

print("\n--- TEMPOS NEGATIVOS ---")
print(dados[dados["Tempo de atendimento (h)"] < 0])

print("\n--- VALIDAÇÃO DOS DADOS ---")

erros = validar_dados(dados)

if erros:
    print("Foram encontrados problemas:")

    for erro in erros:
        print(f"- {erro}")

else:
    print("Todos os dados estão válidos!")