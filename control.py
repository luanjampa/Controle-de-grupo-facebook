import urllib.request
import json
keywords =  ['a','b','sdsds',
            'dfdfo','aff','meu telefone',
            'email','porra','faaa',
            'test','interessado','puts'] # palavras que serão buscadas pelo programa
#em https://developers.facebook.com/tools/explorer
url = 'https://graph.facebook.com/367875099923704/feed?access_token=<token>'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
postagem = data['data'][0]
comentarios = postagem['comments']

for comentario in comentarios['data']:
    dados = comentario['from']
    nome = dados['name']
    codigo = comentario['id']
    mensagem = comentario['message']
    for x in keywords:
        if x in mensagem:
            print("ID: %s NOME: %s MENSAGEM: %s" %(codigo,nome,mensagem))
