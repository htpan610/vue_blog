from django.shortcuts import render
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleListSerializer
# Create your views here.

def article_list(request):
    articles=Article.objects.all()
    serializer=ArticleListSerializer(articles,many=True)
    return JsonResponse(serializer.data,safe=False)