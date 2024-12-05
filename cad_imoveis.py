from numpy import double
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("Win")
pyautogui.write("imobz")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("bps4042")
pyautogui.press("enter")

time.sleep(5)
pyautogui.click(x=1098, y=590)

time.sleep(5)
pyautogui.click(x=1098, y=590)

time.sleep(5)
pyautogui.click(x=50, y=34)

time.sleep(5)
pyautogui.click(x=74, y=120)

time.sleep(5)
pyautogui.click(x=661, y=242)

# time.sleep(1)
# pyautogui.write("simas_2007@hotmail.com")

# pyautogui.press("tab")
# pyautogui.write("pao")


# pyautogui.press("tab")
# pyautogui.press("enter")

# time.sleep(5)


import pandas as pd


tabela = pd.read_csv("imoveis.csv")

print(tabela)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "cep"])

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "quadra"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "endereco"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "numero"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "complemento"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "bairro"]))
    pyautogui.press("tab")
    pyautogui.press("tab")

    # pyautogui.write(str(tabela.loc[linha, "cidade"]))
    
    pyautogui.press("tab")

    # pyautogui.write(str(tabela.loc[linha, "uf"]))
    pyautogui.press("tab")

    pyautogui.click(x=1074, y=324)

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.click(x=1074, y=324)
    pyautogui.press("tab")

    # pyautogui.write(str(tabela.loc[linha, "subtipo"]))
    # pyautogui.press("tab")
    pyautogui.click(x=1095, y=537)
    pyautogui.write(str(tabela.loc[linha, "locacao"]))

    pyautogui.click(x=3160, y=59)
    pyautogui.click(x=904, y=578)
    pyautogui.click(x=1168, y=673)

    # obs = str(tabela.loc[linha, "obs"])
    # if obs != "nan":
    #     pyautogui.write(obs)

    # pyautogui.press("tab")
    # pyautogui.press("enter")

    # pyautogui.scroll(50000)
