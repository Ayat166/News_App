from django.shortcuts import render 
import requests
# Create your views here.

def index(request):   
    if 'search' in request.GET and 'btnsearch' in request.GET:
        search=request.GET['search']
        SEARCH_NEWS = "https://newsapi.org/v2/everything?apiKey=bbb83246743a4927bee52dcc7e7fb48e&q="
        s=SEARCH_NEWS+search
        r = requests.get(s)
        res = r.json()
        data = res['articles']
        title = []
        description = []
        image = []
        url = []
        for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
        news = zip(title,description,image,url)
        return render(request,'pages/index.html',{'news':news})
    else:
       r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})
    
    
def genral(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=general&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})
   
def business(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=business&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})
   
def sport(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=sport&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})
   
def technology(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=technology&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})

def entertainment(request):
       r = requests.get('https://newsapi.org/v2/top-headlines?category=entertainment&country=in&apiKey=bbb83246743a4927bee52dcc7e7fb48e')
       res = r.json()
       data = res['articles']
       title = []
       description = []
       image = []
       url = []
       for i in data:
           title.append(i['title'])
           description.append(i['description'])
           image.append(i['urlToImage'])
           url.append(i['url'])
       news = zip(title,description,image,url)
       return render(request,'pages/index.html',{'news':news})
   
         
        