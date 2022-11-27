from django.contrib.sitemaps import Sitemap
from .models import Blog

class PostSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.written_on