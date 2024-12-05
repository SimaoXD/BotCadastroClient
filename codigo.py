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
pyautogui.click(x=1161, y=89)

time.sleep(5)
pyautogui.click(x=35, y=34)

time.sleep(5)
pyautogui.click(x=69, y=189)

# time.sleep(1)
# pyautogui.write("simas_2007@hotmail.com")

# pyautogui.press("tab")
# pyautogui.write("pao")


# pyautogui.press("tab")
# pyautogui.press("enter")

# time.sleep(5)


import pandas as pd


tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "nome"])

    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "cpf"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "rg"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "nasc"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "cidade"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "pais"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "profissao"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "estado_civil"]))
    pyautogui.press("tab")

    pyautogui.click(x=1132, y=563)
    pyautogui.click(x=905, y=593)
    pyautogui.click(x=1083, y=565)

    # obs = str(tabela.loc[linha, "obs"])
    # if obs != "nan":
    #     pyautogui.write(obs)

    # pyautogui.press("tab")
    # pyautogui.press("enter")

    # pyautogui.scroll(50000)
