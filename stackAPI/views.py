from django.shortcuts import render
from django.http import HttpResponse
from .models import Data
from rest_framework import viewsets,mixins
from .serializer import DataSerializer
import requests
from bs4 import BeautifulSoup
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework import filters

# from rest_framework.pagination import PageNumberPagination

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 10

# Create your views here.
class DataApi(viewsets.ModelViewSet):
    # pagination_class = StandardResultsSetPagination
    search_fields = ['id','question']
    filter_backends = (filters.SearchFilter,)
    queryset = Data.objects.all()
    serializer_class = DataSerializer

def fetch(request):
    try:
        res = requests.get('https://stackoverflow.com/questions')
        soup = BeautifulSoup(res.text,"html.parser")

        data = soup.select(".question-summary")

        for d in data:
            quest = d.select_one('.question-hyperlink').getText()
            vote = d.select_one('.vote-count-post').getText()
            views = d.select_one('.views').attrs['title']
            tags = [ i.getText()  for i in (d.select('.post-tags'))]
            datas = Data()
            datas.question = quest
            datas.vote = vote
            datas.views = views
            datas.tags = tags
            datas.save()
        return HttpResponse(f"fetching data into database is successful")
    except Exception as e:
        return HttpResponse(f"fetching data into database is failed due to {e}")
        pass

