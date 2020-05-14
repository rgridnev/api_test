import connectiondata as cd
import requests, json
from base64 import b64decode

def GetToken(user):
    """Функция получения токена Oauth 2"""
    data = {'grant_type': 'client_credentials'}
    client_id = cd.users[user]['id']
    client_secret = cd.users[user]['secret']
    access_token_response = requests.post(cd.token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))
    tokens = json.loads(access_token_response.text)
    return tokens['access_token']

def b64tofile(b64, filename):
    """Функция создния PDF из Base64"""
    bytes = b64decode(b64, validate=True)
    if bytes[0:4] != b'%PDF':
      raise ValueError('Missing the PDF file signature')
    f = open('testdata/'+filename, 'wb')
    f.write(bytes)
    f.close()