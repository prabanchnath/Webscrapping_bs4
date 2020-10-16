from bs4 import BeautifulSoup
import re
from requests import get
import pandas as pd

name = []         
price = []

for x in range(1,6):
    url = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(x)
    response = get(url)
    bs4_flip = BeautifulSoup(response.text, "html.parser")
    master_container = bs4_flip.find_all('div', class_='_1UoZlX')
    for y in master_container:
        tv_name = y.find('div',class_ = '_3wU53n')
        name.insert(0,tv_name)
        tv_price = y.find('div',class_ = '_1vC4OE _2rQ-NK')
        price.insert(0,tv_price)
    

        flip_df = pd.DataFrame({'Name': name,
                        'Price': price})
        

        print(flip_df.head())