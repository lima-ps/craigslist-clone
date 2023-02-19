from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
from requests.compat import quote_plus #handle de url puttin %20 that means "+" in the url search field
import time
from . import models
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):

    search = request.POST.get('search')  #send the response to the html form
    BASE_CRAIGLIST_URL = f'https://losangeles.craigslist.org/search/sss?bundleDuplicates=1&query={quote_plus(search)}#search=1~grid~0~0'
    driver = webdriver.Chrome('C:/Users/phill/Desktop/Estudo/Python/chromedriver.exe')
    driver.get(BASE_CRAIGLIST_URL)
    time.sleep(1)
    #create a search model object to fed our model
    models.Search.objects.create(search=search) #this will send all our search worlds to the table Search on BD

    #get complete url
    #format make a join in the string and quote plus put a + sign in the search (ex: um teste => um+teste)
    #final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    #print(final_url)
   
  
    response = driver.find_elements(By.CLASS_NAME, 'cl-search-result')
    final_posts = []
    for posts in response:
        title = posts.find_elements(By.CLASS_NAME, 'titlestring')
        post_title = []
        for t in title:
            post_title = t.text
        url = posts.find_elements(By.CLASS_NAME, 'titlestring')
        post_url = []
        for u in url:
            post_url = u.get_attribute('href')
        price = posts.find_elements(By.CLASS_NAME, 'priceinfo')
        post_price = []
        for p in price:
            post_price = p.text
        image = posts.find_elements(By.TAG_NAME, 'img')
        post_image = []
        for i in image:  
            post_image = i.get_attribute('src')
        
        final_posts.append((post_title, post_url, post_price, post_image))

    
    #this will be sent to the client
    stuff_for_frontend = {
        'search':search,
        'final_post': final_posts,
    }
    
    return render(request, 'my_app/new_search.html', stuff_for_frontend)