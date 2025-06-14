from django.shortcuts import render, get_object_or_404
from . import views


def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})
