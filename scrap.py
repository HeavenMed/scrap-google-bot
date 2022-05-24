from googletrans import Translator, constants   #  pip3 install googletrans==3.1.0a0
from pprint import pprint
translator = Translator()

from google_play_scraper import app # pip install google-play-scraper

result  = app(
    "com.mojang.minecraftpe",
    lang="pt",
    country="br"
)
#--------------------------------------------------- o que precisamos tirar do link da google play? ------------------------------------------
#precisamos de:
# title, description ,screenshots,
#--------------------------------------------------------------------------------------------------------------------------------------------
titulo = result['title']
description = result['description']
imagens = result['screenshots']
#--------------------------------------------------------------------------------------------------------------------------------------------
tamanho = len(result['screenshots'])
#------------------------------------------------------------------TRADUZINDO--------------------------------------------------------------------
descricaosrc = translator.translate(description, dest="pt")
descricao = descricaosrc.text
#--------------------------------------------------------------------ADICIONANDO  =w720-h310  AOS LINKS------------------------------------------------------------------
listadelinks = []
for j in range(0,tamanho):
    listadelinks.append(result['screenshots'][j] + '=w720-h310')
#------------------------------------------------------------------GERANDO OS DADOS--------------------------------------------------------------------
print("\n")
print("\n")
print(titulo)
print("\n")
print(" \n")
print(" \n")
print(descricao)
print("\n")
print(" \n")
print(" \n")
for i in range(0 , tamanho):
    print( "\n")
    print(listadelinks[i])
    

