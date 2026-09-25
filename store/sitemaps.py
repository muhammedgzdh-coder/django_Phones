from django.contrib.sitemaps import Sitemap
from .models import Phones


class PhoneSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Phones.objects.all()

    def location(self, obj):
        return f"/d/{obj.id}/"