import urllib.request
import json
#copie o formato no exemplo e pegue o access_token
#em https://developers.facebook.com/tools/explorer
proibido = 'pode'
url = 'https://graph.facebook.com/367875099923704/feed?access_token=CAACEdEose0cBAFZCKxA538zDHbLPiQhTznexTZBxhf9oo1pRmiyctBuCzFpanBb8FjVX8MHym9Dh4jEVOKhGR75ZBqf1gduznBcrI6QtHKZC4h7rEmge5cQjStc67UN6YJHklvgeZCZBcwd6isSZCyFXiQR7nlKYfw7dnWuaa4bQRPNxNXsZCiAdFqNlOrSfw8xoswQ3Ltrx5QZDZD'
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






