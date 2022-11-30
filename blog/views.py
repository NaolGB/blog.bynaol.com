from django.shortcuts import render
from .models import Blog
import json


def home(request):
    context = {
        'blogs': Blog.objects.all().order_by('?')
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')

def blog(request, slug):
    context = {
        
    }
    blog = Blog.objects.get(slug=slug)

    title = blog.title

    text = blog.content
    text_js = json.loads(text)

    intro = text_js['intro']
    subsections = text_js['subsections']
    conclusion = text_js['conclusion']
    date = blog.written_on
    image_name = blog.image.name
    description = blog.description
    description = description.replace(' ', '-')

    context = {
        'title': title,
        'intro': intro,
        'subsections': subsections,
        'conclusion': conclusion,
        'written_on': date,
        'image_name': image_name,
        'blogs': Blog.objects.order_by('?')[:3],
        'description' : description
    }

    return render(request, 'blog/blog.html', context)