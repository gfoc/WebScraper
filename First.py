from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    #print(soup.prettify())

   # Product_tags = soup.find_all('h3')
    
    #for tags in Product_tags:
     #   print(tags.text )
    
    Product_cards = soup.find_all('div',class_ = 'product-item')

    for product in Product_cards:
        Name = product.h3.text
        price = product.p.text
        print(f'The {Name} is of {price} including discount')

    

