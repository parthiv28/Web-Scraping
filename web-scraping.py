from bs4 import BeautifulSoup 
from selenium import webdriver
import pandas as pd
import lxml

driver = webdriver.Chrome("chromedriver.exe")
products=[] 
prices=[] 
ratings=[]

for page in range(1, 10):
    driver.get("https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorytree&page=" + str(page))
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')
    for a in soup.findAll(attrs={'class':'_2kHMtA'}):
        name=a.find('div', attrs={'class':'_4rR01T'})
        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        rating=a.find('div', attrs={'class':'_3LWZlK'})
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)
        
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('D19IT147_PARTHIV.csv', index=False, encoding='utf-8')

                        

