#Instalar e importar as bibliotecas
    #pip install pyautogui 

import pyautogui
import time

#Passos:
#1- Entrar no sistema da empresa
#	https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pyautogui.write()
#pyautogui.click()
#pyautogui.press()
#pyautogui.hotkey()

pyautogui.PAUSE = 1

#abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(3)


#digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
time.sleep(2)
pyautogui.press("enter")

#2- Fazer o login
pyautogui.click(x=734, y=481)
pyautogui.write("aboboraaboboraabobora@gamil.com")
pyautogui.press("tab")

pyautogui.write("aaosfjao")
pyautogui.press("tab")

pyautogui.press("enter")

#instalar o pandas
    #pip install pandas numpy openpyxl
#3- Importar a bd
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

#4- Cadastrar um produto
for indice, linha in tabela.iterrows():
    #cadastra o código
    pyautogui.click(x=898, y=335)
    codigo = linha["codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")


    #cadastra a marca
    pyautogui.write(linha["marca"])
    pyautogui.press("tab")

    #cadastra o tipo
    pyautogui.write(linha["tipo"])
    pyautogui.press("tab")

    #cadastra a categoria
    pyautogui.write(str(linha["categoria"]))
    pyautogui.press("tab")

    #cadastra o preco
    pyautogui.write(str(linha["preco_unitario"]))
    pyautogui.press("tab")

    #cadastra o custo
    pyautogui.write(str(linha["custo"]))
    pyautogui.press("tab")

    #cadastra a observação (se houver)
    obs = linha["obs"]
    if not pd.isna(obs):
        pyautogui.write(linha["obs"])

    #finaliza
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.press("home")


#5- Repetir o passo 4 até acabar

