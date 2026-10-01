from django.contrib.sitemaps import Sitemap
from .models import Phones
from django.urls import reverse

class PhoneSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Phones.objects.filter(status=True).order_by('-created_date')[:3]

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.update_date
    

    

class ViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'


    def items(self):
        return ['store:products','store:brands']

    def location(self, item):
        return reverse(item)