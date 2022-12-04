from django.shortcuts import render
from blog.models import Blog

def error500(request):
    description = "Health-and-Fitness-blog-offering-expert-advice-on-everything-from-diet-and-nutrition-to-exercise-tips-and-healthy-lifestyle-habits-to-help-you-reach-your-goals."
    context = {
        'top_blogs': Blog.objects.filter(published=True).order_by('?')[:8],
        'description' : description
    }
    return render(request, 'error_500.html', context=context)

def error404(request, exception):
    description = "Health-and-Fitness-blog-offering-expert-advice-on-everything-from-diet-and-nutrition-to-exercise-tips-and-healthy-lifestyle-habits-to-help-you-reach-your-goals."
    context = {
        'top_blogs': Blog.objects.filter(published=True).order_by('?')[:8],
        'description' : description
    }
    return render(request, 'error_404.html', status=404, context=context)