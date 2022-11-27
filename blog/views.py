from django.shortcuts import render
from .models import Blog
import json


def home(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')

def blog(request, slug):
    title = Blog.objects.get(slug=slug).title

    text = Blog.objects.get(slug=slug).content
    text_js = json.loads(text)

    intro = text_js['intro']
    subsections = text_js['subsections']
    conclusion = text_js['conclusion']
    date = Blog.objects.get(slug=slug).written_on
    image_name = Blog.objects.get(slug=slug).image.name

    context = {
        'title': title,
        'intro': intro,
        'subsections': subsections,
        'conclusion': conclusion,
        'written_on': date,
        'image_name': image_name
    }

    return render(request, 'blog/blog.html', context)