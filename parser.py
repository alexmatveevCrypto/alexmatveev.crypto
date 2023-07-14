try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
html = #the HTML code you've written above
parsed_html = BeautifulSoup(html)
print(parsed_html.body.find('div', attrs={'class':'container'}).text)
