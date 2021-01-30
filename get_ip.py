from requests import get

#use get to get ip adress from ipify.org
ip= get("https://api.ipify.org/").text

#print IP address
print("Your IP Address is", ip)
