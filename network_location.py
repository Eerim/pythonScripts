import json
from urllib.request import urlopen

#get response
response=urlopen('http://ipinfo.io/json')

#store reponse
data=json.load(response)

#print response via formating
print('{:<15}|{:<}'.format('IP Address',data['ip']))
print('{:<15}|{:<}'.format('Server',data['org']))
print('{:<15}|{:<}'.format('City',data['city']))
print('{:<15}|{:<}'.format('Country',data['country']))
print('{:<15}|{:<}'.format('Region',data['region']))
print('{:<15}|{:<}'.format('Time zone',data['timezone']))

    