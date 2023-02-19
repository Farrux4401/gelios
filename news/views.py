from django.shortcuts import render
from requests import request
from .models import *
from django.views.generic import ListView
# Create your views here.


def home(request):
    latest_new = New.objects.filter().order_by('-id')[0:1]
    other_news = New.objects.filter().order_by('-id')[0:6]
    categories = Category.objects.all()
    regions = Region.objects.all()

    context = {
        'latest_new': latest_new,
        'other_news': other_news,
        'categories': categories,
        'regions': regions
    }
    return render(request, 'home.html', context)


def detail(request, id):
    news = New.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = New.objects.filter(category=category).exclude(id=id)
    latest_news = New.objects.filter().order_by('-id')[0:6]
    categories = Category.objects.all()
    regions = Region.objects.all()
    lugat = {
        'news': news,
        'category': category,
        'rel_news': rel_news,
        'latest_news': latest_news,
        'categories': categories,
        'regions': regions,
    }
    return render(request, 'detail.html', lugat)


class AllNews(ListView):
    model = New
    template_name = 'all_news.html'


def category(request, id):
    category = Category.objects.get(id=id)
    news = New.objects.filter(category=category)
    categories = Category.objects.all()
    regions = Region.objects.all()
    return render(request, 'category_news.html', {
        'category': category,
        'news': news,
        'categories': categories,
        'regions': regions,
    })


def region(request, id):
    region = Region.objects.get(id=id)
    news = New.objects.filter(region=region)
    categories = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'region': region,
        'news': news,
        'categories': categories,
        'regions': regions,
    }
    return render(request, 'region_news.html', context)
