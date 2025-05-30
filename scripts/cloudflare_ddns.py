import secret
import requests

ip_r = requests.get('http://icanhazip.com/') # TODO: use https://cloudflare.com/cdn-cgi/trace
ip = ip_r.text.strip()

headers = {'X-Auth-Email': secret.CF['email'],
           'X-Auth-Key':   secret.CF['key'],
           'Content-Type': 'application/json'}

params = {'type':    'A',
          'name':    'den.rexy.xyz',
          'content': ip}

slugs = {'endpoint': 'https://api.cloudflare.com/client/v4',
         'zone_id':  secret.HOME['zone_id'],
         'id':       secret.HOME['id']}
url = '{endpoint}/zones/{zone_id}/dns_records/{id}'.format(**slugs)

r = requests.put(url, headers=headers, json=params)

if r.json()['success'] == True:
    print('updated')
