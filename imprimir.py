import win32print
import win32api
import os

import time

lista_impressoras = win32print.EnumPrinters(6)

impressora = lista_impressoras[5]

win32print.SetDefaultPrinter(impressora[2])

caminho = r"C:\Users\user\Downloads\imprimir"

lista_arquivos = os.listdir(caminho)

print(lista_arquivos )

lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

time.sleep(30)
dir = r'C:\Users\user\Downloads\imprimir'
for f in os.listdir(dir):
   os.remove(os.path.join(dir, f))


#for arquivo in lista_arquivos:
 #   win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

##for impressora in lista_impressoras:
  #  print(impressora)