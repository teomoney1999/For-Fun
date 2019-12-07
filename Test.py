from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

try:
    driver = webdriver.Safari()
except: 
    print('Driver not found')


products = []
prices = [] 
ratings = []
# Open the URL
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")


# Extract data from the website
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', href=True, attr={'class':'_31qSD5'}):
    name = a.find('div', attr={'class':'_3wU52n'})
    price = a.find('div', attr={'class':'_1vC4OE _2rQ-NK'})
    rating = a.find('div', attr={'class':'hGSR34'})
    products.append(name)
    prices.append(price)
    ratings.append(rating)


# Formating data 
df = pd.DataFrame({'Product Name':products, 'Price':prices,'Rating':ratings})
df.to_csv("products2.csv", index=False, encoding='utf-8')
