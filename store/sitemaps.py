from django.contrib.sitemaps import Sitemap
from .models import Phones


class PhoneSitemap(Sitemap):

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Phones.objects.filter(status=True)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.update_date