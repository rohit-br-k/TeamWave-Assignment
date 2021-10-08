from django.shortcuts import render
from stackAPI.models import Data
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def home(request):
    data = Data.objects.all()
    paginator = Paginator(data,5)
    page = request.GET.get('page')
    paged_data = paginator.get_page(page)
    context = {
        "data":paged_data,
    }
    return render(request,"home.html",context)

def search(request):
    data = Data.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            data = data.filter(question__icontains=keyword)
    context = {
        "searched":data,
    }
    return render(request,"search.html",context)
