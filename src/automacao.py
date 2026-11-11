
import pyautogui
import pyperclip
import pygetwindow as gw
import time
from pathlib import Path


def selecionar_intervalo(intervalo):

    # Abre a janela Ir Para
    pyautogui.press("f5")
    time.sleep(1)

    # Informa o intervalo desejado
    pyperclip.copy(intervalo)
    pyautogui.hotkey("ctrl", "v")

    # Confirma a seleção
    pyautogui.press("enter")
    time.sleep(1)

    # Auto ajuste
    pyautogui.hotkey("alt", "c", "o", "t")
    time.sleep(2)


def criar_grafico(intervalo):

    # Seleciona os dados do resumo
    selecionar_intervalo(intervalo)

    # Transforma os dados em uma tabela
    pyautogui.hotkey("ctrl", "alt", "t")
    time.sleep(2)

    # Confirma a criação da tabela
    pyautogui.press("enter")
    time.sleep(2)

    # Cria o gráfico
    pyautogui.hotkey("alt", "f1")
    time.sleep(2)


def formatar_relatorio():

    try:
        # Acessa a aba Atendimentos
        pyautogui.hotkey("ctrl", "pagedown")
        time.sleep(1)

        # Seleciona todos os dados utilizados
        pyautogui.hotkey("ctrl", "home")
        pyautogui.hotkey("ctrl", "shift", "end")
        time.sleep(1)

        # Transforma os dados em uma tabela
        pyautogui.hotkey("ctrl", "alt", "t")
        time.sleep(2)

        # Confirma a criação da tabela
        pyautogui.press("enter")
        time.sleep(2)

        # Auto ajuste
        pyautogui.hotkey("alt", "c", "o", "t")
        time.sleep(2)

        # Salva o relatório
        pyautogui.hotkey("ctrl", "b")
        time.sleep(2)

        print("Relatório formatado e salvo com sucesso!")
        return True

    except Exception as erro:
        print(f"Erro ao formatar o relatório: {erro}")
        return False



def abrir_arquivo(caminho_arquivo, intervalo_grafico):

    caminho_arquivo = Path(caminho_arquivo)

    if not caminho_arquivo.exists():
        print("Arquivo não encontrado.")
        return False

    try:
        # Abre o Explorador de Arquivos
        pyautogui.hotkey("win", "e")
        time.sleep(2)

        # Acessa a barra de endereço
        pyautogui.hotkey("ctrl", "l")

        # Informa o caminho completo do arquivo
        pyperclip.copy(str(caminho_arquivo))
        pyautogui.hotkey("ctrl", "v")

        # Abre o arquivo no programa padrão
        pyautogui.press("enter")

        # Aguarda a abertura do relatório
        print("Aguardando abertura do relatório...")

        nome_arquivo = caminho_arquivo.stem.lower()

        for tentativa in range(15):

            janelas = gw.getAllTitles()

            arquivo_aberto = any(
                nome_arquivo in janela.lower()
                for janela in janelas
            )

            if arquivo_aberto:
                print("Relatório aberto com sucesso!")

                # Localiza a janela do relatório
                janelas_excel = gw.getWindowsWithTitle(nome_arquivo)

                if not janelas_excel:
                    print("Não foi possível localizar a janela do Excel.")
                    return False

                janela_excel = janelas_excel[0]

                if janela_excel.isMinimized:
                    janela_excel.restore()

                janela_excel.activate()
                time.sleep(2)

                # Cria o gráfico na aba Resumo
                criar_grafico(intervalo_grafico)

                # Formata a aba Atendimentos e salva
                return formatar_relatorio()

            time.sleep(1)

        print("Erro: não foi possível confirmar a abertura do relatório.")
        return False

    except Exception as erro:
        print(f"Erro durante a automação: {erro}")
        return False
