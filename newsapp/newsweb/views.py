from django.shortcuts import render

def homepage(request):
    import requests
    import json

    news_api_req = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4cbf5645264840fb96e4c5695ee6e312")
    api = json.loads(news_api_req.content)
    return render(request, 'newsweb/home.html', {'api': api})


