import pyautogui as pg
import time

#Passo 01 - Pegar a posição na tela
#Posicao do arquivo na tela: x=719, y=205
time.sleep(1)
#print(pg.position())
#x, y = pg.position()

#Passo 02: mover o mouse para a posição
pg.moveTo(607, 172, 2)
time.sleep(1)
#Passo 03: Executar duplo clique
pg.doubleClick(607, 172)
time.sleep(1)
#Passo 04: Escrever algo
pg.hotkey("win", "up")
time.sleep(1)
pg.typewrite("Aula de Programacao no Sabado")
time.sleep(1)
pg.press("enter")
pg.typewrite("Quem perdeu ")
time.sleep(1)
pg.typewrite("VACILOU!")
time.sleep(3)

#Passo 05: Salvar
pg.hotkey("Ctrl", "S")
time.sleep(1)

#Passo 06: Nomear o arquivo
pg.typewrite("agenda")
time.sleep(1)

#Passo 07: Clicar enter
pg.press("enter")
time.sleep(1)

#Passo 08: Fechar a tela
pg.hotkey("alt", "F4")
time.sleep(1)


