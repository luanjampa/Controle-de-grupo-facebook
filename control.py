import urllib.request
import json
#copie o formato no exemplo e pegue o access_token
#em https://developers.facebook.com/tools/explorer
proibido = 'pode'
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
    print("ID: %s NOME: %s MENSAGEM: %s" %(codigo,nome,mensagem))






