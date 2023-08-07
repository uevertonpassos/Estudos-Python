import os
import datetime
from pathlib import Path
import subprocess
import platform
import getpass

def criar_log(caminho_pasta):
    # Comando para executar no terminal do Windows
    comando = "ipconfig /flushdns"

    # Pega a data do sistema
    dataAtual = datetime.datetime.now()

    # Cria o arquivo de log com a data atual do sistema
    nomeArquivo = dataAtual.strftime("%d-%m-%Y")

    # Define o caminho da pasta onde o log será guardado
    caminho_pasta = Path(caminho_pasta) if caminho_pasta else Path(os.path.expanduser('~'), 'Documents', 'confirmação-de-logs')

    # Cria a pasta se não existir
    caminho_pasta.mkdir(parents=True, exist_ok=True)

    # Define o caminho completo para o arquivo de log
    caminhoLog = caminho_pasta / f"{nomeArquivo}.txt"

    # Cria o arquivo de log se não existir
    if not caminhoLog.exists():
        caminhoLog.touch()

    # Escreve no arquivo de log
    with caminhoLog.open(mode='a') as log_file:
        log_file.write("-----------------------------------------------------------------------------\n")
        log_file.write(dataAtual.strftime("%H:%M:%S") + "\n")
        subprocess.run(comando, shell=True, stdout=log_file, stderr=log_file)

def adicionar_aplicativo_inicializacao():
    sistema = platform.system()

    if sistema == "Windows":
        caminho_script = os.path.join(os.path.expanduser('~'), 'Documents', 'startup_app.bat')

        # Cria um arquivo .bat que executa o código Python na inicialização
        with open(caminho_script, 'w') as bat_file:
            bat_file.write('@echo off\n')
            bat_file.write('python "{}"\n'.format(os.path.abspath(__file__)))

        # Configura o arquivo .bat como um aplicativo de inicialização
        caminho_inicializacao = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        caminho_destino = os.path.join(caminho_inicializacao, 'startup_app.bat')
        os.replace(caminho_script, caminho_destino)

    elif sistema == "Linux":
        caminho_script = os.path.join(os.path.expanduser('~'), 'Documents', 'startup_app.sh')

        # Cria um arquivo .sh que executa o código Python na inicialização
        with open(caminho_script, 'w') as sh_file:
            sh_file.write('#!/bin/bash\n')
            sh_file.write('python "{}"\n'.format(os.path.abspath(__file__)))

        # Torna o arquivo .sh executável
        os.chmod(caminho_script, 0o755)

        # Adiciona o script como um aplicativo de inicialização
        caminho_inicializacao = os.path.join(os.path.expanduser('~'), '.config', 'autostart')
        caminho_destino = os.path.join(caminho_inicializacao, 'startup_app.desktop')

        with open(caminho_destino, 'w') as desktop_file:
            desktop_file.write('[Desktop Entry]\n')
            desktop_file.write('Type=Application\n')
            desktop_file.write('Exec={}\n'.format(caminho_script))
            desktop_file.write('X-GNOME-Autostart-enabled=true\n')

    else:
        print("Sistema operacional não suportado para adicionar aplicativo de inicialização.")

if __name__ == "__main__":
    # Chama a função para criar o arquivo de log
    criar_log(None)  # Se você quiser especificar um caminho de pasta diferente, coloque-o dentro do parênteses.

    # Chama a função para adicionar o aplicativo de inicialização
    adicionar_aplicativo_inicializacao()

#PODE SUBIR