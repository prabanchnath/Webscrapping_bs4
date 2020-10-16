from bs4 import BeautifulSoup
import re
from requests import get
import pandas as pd

name = []         
price = []

for x in range(1,6):
    url = "https://www.flipkart.com/search?q=tv&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(x)       #Fetching the url
    response = get(url)
    bs4_flip = BeautifulSoup(response.text, "html.parser")          #storing the text part of the site in html format
    master_container = bs4_flip.find_all('div', class_='_1UoZlX')   
    for y in master_container:
        tv_name = y.find('div',class_ = '_3wU53n')          #accessing the name 
        name.insert(0,tv_name)                              #inserting name into the empty list
        tv_price = y.find('div',class_ = '_1vC4OE _2rQ-NK') #accessing the price
        price.insert(0,tv_price)                            #inserting the price into the empty list
    

        flip_df = pd.DataFrame({'Name': name, 
                        'Price': price})                    #created a dataframe
        

        print(flip_df.head())