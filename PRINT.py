# BIBLIOTECAS
from IPython.display import clear_output
from importlib import util
from pathlib import Path

import subprocess
import time 
import os

# ATUALIZAR O PYTHON
subprocess.check_call(["python", "-m", "pip", "install", "--upgrade", "pip"])

# ATUALIZAR UMA BIBLIOTECA
biblioteca = 'importlib'

try:
    subprocess.check_call(["pip", "install", "--upgrade", biblioteca])
except subprocess.CalledProcessError as e:
    print(f"Failed to upgrade {biblioteca}: {e}")

pacote = "pyautogui" 

# ACHAR O CAMINHO ABSOLUTO DA PASTA
pasta = Path().absolute()

# AJUSTAR NOME DO ARQUIVO PARA LEITIRA
newpath = str(pasta) + '/print.txt'
newpath = newpath.replace("\\","/")

# FUNÇÃO PARA LER O CSV
def LerTxt():
    try:
         with open(newpath, "r") as arquivo:
            conteudo = arquivo.read()
            arquivo.close()
            return conteudo
    except:
        arquivo = open(newpath,'a')
        arquivo.write('1')
        arquivo.close()
        conteudo = '1'
        return conteudo

# FUNÇÃO DE PRINT
def Print():
    if util.find_spec("pyautogui") is not None:
        from pyautogui import press
        press("ctrl")
        time.sleep(120)
    else:
        subprocess.check_call(["pip", "install", pacote])
        from pyautogui import press
        press("ctrl")
        time.sleep(120)

# VALOR INICIAL
valor = LerTxt()

clear_output()

# LOOP
print('Rodando o Print')

while valor == '1':
    Print()
    valor = LerTxt()
    
print('Print finalizado')
time.sleep(10)
## certo