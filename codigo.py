# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
       # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5    
# pyautogui.click -> Clicar em algum lugar da tela 
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Pressionar 1 tecla do tecla
# pyautogui.hotkey("ctrl","v")
# Abrir um navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
# Dar uma pausa um pouco maior (3s)
time.sleep(3)
# Passo 2: Fazer o login
pyautogui.click(x=932, y=472)
pyautogui.write("developer_danilo@gmail.com")
# Escrever a senha
pyautogui.press("tab")
pyautogui.write("0100101001010011011001")
# clicar no botão de logar
pyautogui.click(x=941, y=683)
time.sleep(3)
# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4: Cadastrar 1 produto
# Para cada linha da tabela
for linha in tabela.index:
       # clicar no primeiro campo
       pyautogui.click(x=869, y=321)
       # Código do produto
       codigo = tabela.loc[linha, "codigo"]
       pyautogui.write(codigo)
       pyautogui.press("tab")      
       # marca
       pyautogui.write(tabela.loc[linha, "marca"])
       pyautogui.press("tab")
       # tipo
       pyautogui.write(tabela.loc[linha, "tipo"])
       pyautogui.press("tab")
       # categoria
       # str = () String -> texto
       # str(1) -> 1 -> "1"
       pyautogui.write(str(tabela.loc[linha, "categoria"]))
       pyautogui.press("tab")
       # Preço
       pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
       pyautogui.press("tab")
       # Custo 
       pyautogui.write(str(tabela.loc[linha, "custo"]))
       pyautogui.press("tab")
       # Obs
       obs = tabela.loc[linha, "obs"]
       if not pandas.isna(obs):
              pyautogui.write(obs)
       # enviar
       pyautogui.press("enter")
       pyautogui.scroll(5000)
# Passo 5: Repetir o processo de cadastro até acabar
      