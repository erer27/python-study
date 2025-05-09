from urllib import response

import requests
from bs4 import BeautifulSoup

def recipe():

    url=f"https://www.10000recipe.com/recipe/list.html?or"
    res_html=requests.get(url)
    recipe_data=res_html.text
    print(recipe_data)
    soup=BeautifulSoup(recipe_data,'html.parser')
    title=soup.select(',common_sp_caption .common_sp_caption')
    chef=soup.select('.common_sp_caption')
    img=soup.select('.common_sp_thumb .common_sp_link img')
    hit=soup.select('.common_sp_caption_buyer')
    print(title)
    for i in range(0,len(title)):
        print(title[i].text)
        print(chef[i].text)
        print(hit[i].text)
        print(img[i].attrs['src'])
