from django import template
from result.models import Phones

register = template.Library()


@register.inclusion_tag('tags_brands.html')
def Tag_brands():

    brands = set()
    phones = Phones.objects.all()
    for phone in phones:
        for tag in phone.tags.all():
            brands.add(tag)

    return {'brands': brands}

@register.inclusion_tag('tags_memory.html')
def Tag_memory():

    memory = Phones.objects.values_list(
        'memory',
        flat=True
    ).distinct()

    return {
        'memory': memory
    }
    

@register.inclusion_tag('tags_network.html')
def Tag_network():

    Network = Phones.objects.values_list('network',flat=True).distinct()
    
    return {'Network': Network}
        
