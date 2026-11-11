# Automação de Relatórios de Atendimentos de TI

Projeto desenvolvido em Python para automatizar a leitura, validação e
geração de relatórios a partir de registros de atendimentos de
Tecnologia da Informação (TI) armazenados em uma planilha Excel.

A solução simula um cenário de suporte técnico, utilizando dados
fictícios para demonstrar como a automação pode reduzir etapas manuais,
padronizar informações e facilitar a visualização dos atendimentos.

## Objetivo

Automatizar parte do processo de consolidação de registros de
atendimento de TI, desde a leitura e validação dos dados até a criação e
formatação de um relatório no Microsoft Excel.

## Funcionalidades

-   Leitura de registros de atendimento armazenados em uma planilha
    Excel.
-   Verificação da estrutura e dos dados de entrada.
-   Validação de campos obrigatórios e identificação de inconsistências,
    como IDs duplicados e valores fora dos padrões definidos.
-   Geração automática de um arquivo de relatório com data e hora no
    nome.
-   Criação de uma planilha de resumo e inclusão dos registros de
    atendimento.
-   Automação de ações na interface gráfica do Windows e do Excel com
    PyAutoGUI.
-   Formatação de tabelas, ajuste de colunas e criação de gráfico no
    Excel.
-   Mensagens para orientar o usuário em situações de erro, como quando
    a planilha de origem não pode ser acessada.

## Tecnologias utilizadas

  -----------------------------------------------------------------------
  Tecnologia                          Utilização
  ----------------------------------- -----------------------------------
  Python 3.11                         Linguagem utilizada no
                                      desenvolvimento da solução.

  Pandas                              Leitura, manipulação e validação
                                      dos dados tabulares.

  OpenPyXL                            Integração com arquivos Excel por
                                      meio do Pandas.

  PyAutoGUI                           Automação de ações na interface
                                      gráfica.

  PyGetWindow                         Identificação e ativação da janela
                                      do Excel.

  Pyperclip                           Apoio à transferência de texto para
                                      a área de transferência.

  Microsoft Excel                     Abertura, formatação e visualização
                                      do relatório.
  -----------------------------------------------------------------------

## Estrutura do projeto

``` text
AutomacaoRelatoriosTI/
├── dados/
│   └── atendimentos.xlsx
├── relatorios/
├── src/
│   ├── inspecionar_dados.py
│   ├── processamento.py
│   ├── automacao.py
│   └── main.py
├── bizagi/
│   ├── Fluxo_Automacao_Relatorios.bpm
│   └── Fluxo_Automacao_Relatorios.pdf
├── requirements.txt
├── POP-TI-001_Automacao-de-Relatorios.docx
└── README.md
```

-   `dados/`: contém a planilha de entrada.
-   `relatorios/`: destino dos relatórios gerados.
-   `src/`: reúne os módulos Python da aplicação.
-   `bizagi/`: contém o modelo do processo e sua versão em PDF.
-   `requirements.txt`: lista as dependências Python do projeto.
-   `POP-TI-001_Automacao-de-Relatorios.docx`: procedimento operacional
    padrão (POP) da automação.

## Como executar

### 1. Pré-requisitos

-   Windows 10 ou 11.
-   Python 3.11.
-   Microsoft Excel instalado.
-   Git (opcional, para clonar o repositório).

### 2. Obter o projeto

Clone o repositório:

``` bash
git clone https://github.com/IsabelleRancan/AutomacaoRelatoriosTI
cd AutomacaoRelatoriosTI
```

Ou baixe os arquivos do repositório e abra a pasta do projeto.

### 3. Criar e ativar o ambiente virtual

No PowerShell:

``` powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

``` powershell
pip install -r requirements.txt
```

### 5. Preparar a planilha de entrada

Verifique se o arquivo `atendimentos.xlsx` está dentro da pasta `dados/`
e se contém a aba `ATENDIMENTOS` com as colunas esperadas:

-   `ID`
-   `Data de abertura`
-   `Categoria`
-   `Descrição`
-   `Prioridade`
-   `Status`
-   `Tempo de atendimento (h)`

O projeto utiliza dados fictícios para fins demonstrativos. Caso
substitua a planilha, mantenha a estrutura esperada e os valores
compatíveis com as regras de validação implementadas.

### 6. Executar a automação

**Importante:** antes de executar, feche a planilha original
`dados/atendimentos.xlsx` no Excel. O arquivo precisa estar fechado para
que a automação consiga acessá-lo corretamente.

Com o ambiente virtual ativado, execute:

``` powershell
python src/main.py
```

Ao final do processo, o relatório será salvo na pasta `relatorios/` com
um nome que inclui a data e o horário de geração. O arquivo será aberto
no Excel para que o resultado possa ser conferido.

## Saída gerada

O relatório contém duas planilhas:

-   **Resumo:** apresenta a consolidação dos atendimentos por status e
    um gráfico.
-   **Atendimentos:** reúne os registros utilizados na geração do
    relatório.

O arquivo de saída segue o padrão:

``` text
relatorio_atendimentos_AAAAMMDD_HHMMSS.xlsx
```

## Documentação do processo

Além do código, o projeto inclui materiais de documentação:

-   **POP:** descreve os pré-requisitos, as etapas de execução, os
    cuidados operacionais e o tratamento de situações de erro.
-   **Fluxo do processo (Bizagi):** representa visualmente as etapas e
    decisões do processo de geração dos relatórios.
-   **Referências conceituais:** o projeto considera conceitos
    relacionados ao gerenciamento de serviços de TI da ITIL 4 e ao
    objetivo DSS02 do COBIT 2019, ligado ao gerenciamento de
    solicitações de serviço e incidentes.

> **Observação:** ITIL 4 e COBIT 2019 foram utilizados como referências
> conceituais. O projeto não implementa integralmente esses frameworks
> nem substitui uma ferramenta de gerenciamento de serviços ou chamados.

## Limitações e possibilidades de evolução

Esta é uma aplicação demonstrativa, construída com dados fictícios e
regras definidas para o cenário proposto. A automação da interface
depende da disponibilidade do Windows e do Microsoft Excel, e pode
exigir ajustes caso haja mudanças na resolução da tela, na versão do
Excel ou na disposição das janelas.

Como possibilidades de evolução, podem ser considerados:

-   Inclusão de indicadores adicionais, como tempo médio de atendimento.
-   Análises por categoria, prioridade e período.
-   Ampliação das regras de validação.
-   Adaptação para diferentes estruturas de planilhas.
-   Integração futura com fontes de dados ou sistemas de chamados.

## Finalidade

Projeto desenvolvido para fins de estudo e demonstração de conhecimentos
em Python, manipulação e validação de dados, automação de interface
gráfica e documentação de processos de TI.
