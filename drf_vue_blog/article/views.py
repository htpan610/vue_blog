from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from .models import Article
from .serializers import ArticleListSerializer
# Create your views here.

def article_list(request):
    articles=Article.objects.all()
    serializer=ArticleListSerializer(articles,many=True)
    return JsonResponse(serializer.data,safe=False)

def home(request):
    return render(request, 'home.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })