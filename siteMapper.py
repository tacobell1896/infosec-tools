import requests
from bs4 import BeautifulSoup
url = input("Please enter a domain name: ")
addSiteMap = "http://" + url + "/sitemap.xml"
page = requests.get(addSiteMap)
sitemap_index = BeautifulSoup(page.content, 'html.parser')
urls = [element.text for element in sitemap_index.findAll('loc')]
print(urls)
