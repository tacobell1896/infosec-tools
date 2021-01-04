import mechanize
from bs4 import BeautifulSoup as bsoup
import sys
##url = input("Please enter a domain name: ")
##addSiteMap = "http://" + url + "/sitemap.xml"
#page = requests.get(addSiteMap)
#sitemap_index = bsoup(page.content, 'html.parser')
#urls = [element.text for element in sitemap_index.findAll('loc')]
#print(urls)

def filterSoup( html ):
    data_ = [ ]
    page = bsoup( html )
    for link in page.findAll( 'a' ):
        data_.append( link.get( 'href' ) )
    for link in page.findAll( 'form' ):
        data_.append( link.get( 'action' ) )
    return data_

def browser( link ):
    browser = mechanize.Browser()
    document = browser.open( link )
    if document.code < 400:
        html = document.read()
        list_ = filterSoup( html )
        return list_
    else:
        print ("Error Code: ", document.code)
        import sys
        sys.exit(1)

def main():
    tgt = sys.argv[1]
    links__ = browser( str( tgt ) )
    if len( links__ ) == 0:
        sys.exit( 'Nothing found in the Document' )
    else:
        for link_ in links__:
            print(link_)

if __name__ == "__name__":
    main()