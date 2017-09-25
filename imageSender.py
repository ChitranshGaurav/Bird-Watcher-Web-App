import requests

url = "http://localhost/imageOpener.py"
files = open('blue-winged-warbler.jpg', 'rb')

r = requests.post(url, data=files)
print r