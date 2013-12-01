##!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Luan Pacote
#contact: 
import json,requests

def ListarPublicacao(comentarios,cont):
    comentarios = postagem['comments']
    for comentario in comentarios['data']:
        dados = comentario['from']
        nome = dados['name']
        codigo_usuario = dados['id']
        #codigo_publicacao = comentario['id'] usar para pegar a o link direto que o usuario comentou
        mensagem = comentario['message']
        mensagem = mensagem.lower()
        for x in keywords:
            if x in mensagem:
                print("ID: %s NOME: %s MENSAGEM: %s" %(codigo_usuario,nome,mensagem)

keywords =  ['','',''] # palavras que serão buscadas pelo programa
#em https://developers.facebook.com/tools/explorer
token = ""
url = requests.get("https://graph.facebook.com/367875099923704/feed?access_token=" + token)
resp = url.json()
ini = 0 #em que postagem inicia a busca, lembrando que o indice comeca do 0
fim = 8 # limite de postagem que sera buscada, o facebook so libera ate 9 paginas por vez, ou seja de 0 a 8
while ini <= fim:
    try:
        postagem = resp['data'][ini]
        ListarPublicacao(postagem,ini)
    except:
        print('')
    ini += 1



#r = requests.delete("/367875099923704/members/100003481959842")


