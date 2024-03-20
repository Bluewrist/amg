from django.contrib.sitemaps import Sitemap
from .models import Product
from django.urls import reverse
 
 
class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.date
        
    def location(self,obj):
        return '/product_detail/%s' % (obj.id)




class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home','contact']

    def location(self, item):
        return reverse(item)