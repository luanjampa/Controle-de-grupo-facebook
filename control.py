##!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Este programa é um software livre; você pode redistribuí-lo e/ou

    modificá-lo dentro dos termos da Licença Pública Geral GNU como

    publicada pela Fundação do Software Livre (FSF); na versão 2 da

    Licença, ou (na sua opinião) qualquer versão.



    Este programa é distribuído na esperança de que possa ser útil,

    mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO a qualquer

    MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a

    Licença Pública Geral GNU para maiores detalhes.



    Você deve ter recebido uma cópia da Licença Pública Geral GNU

    junto com este programa, se não, escreva para a Fundação do Software

    Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

#author: Luan Pacote
#contact: lsouza
import urllib,urllib.request,json

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
                print("ID: %s NOME: %s MENSAGEM: %s" %(codigo_usuario,nome,mensagem))





keywords =  ['','',''] # palavras que serão buscadas pelo programa
#em https://developers.facebook.com/tools/explorer
token = ""
url ="https://graph.facebook.com/367875099923704/feed?access_token=" + token
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
ini = 0 #em que postagem inicia a busca, lembrando que o indice comeca do 0
fim = 8 # limite de postagem que sera buscada, o facebook so libera ate 9 paginas por vez, ou seja de 0 a 8
while ini <= fim:
    try:
        postagem = data['data'][ini]
        ListarPublicacao(postagem,ini)
    except:
        print('')
    ini += 1

