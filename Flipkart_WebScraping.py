from bs4 import BeautifulSoup
import requests
import pandas as pd

product_name =[]
price =[]
description =[]


for i in range(1,60):
    url = 'https://www.flipkart.com/search?q=laptop+under+200000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(i)

    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml') 
    box = soup.find('div',class_ = '_1YokD2 _3Mn1Gg')

    names = box.find_all('div',class_ = '_4rR01T')
    for i in names:
        product_name.append(i.text)


    cost = box.find_all('div',class_ = '_30jeq3 _1_WHN1')
    for i in cost:
        price.append(i.text)


    des = box.find_all('div',class_ = 'fMghEO')
    for i in des:
        description.append(i.text)

print(product_name)
print(price)
print(description)

data = pd.DataFrame({'Product_Name':product_name,'Price':price,'Description':description})


data.to_csv('E:/DS And Python/Data Science/Project/Flipkart-Web Scraping/Laptop_Under_200000.csv')