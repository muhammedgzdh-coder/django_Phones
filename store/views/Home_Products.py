from django.shortcuts import render , redirect ,get_object_or_404
from store.models.post import Phones
from taggit.models import Tag
from store.selector.tags import Tags 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.cache import cache

def home(request):

    # -------------------------
    # Latest 3 Phones
    # -------------------------

    phones_data = cache.get("home:latest_phones")

    if phones_data is None:
        print("PHONES CACHE MISS")

        phones = (Phones.objects.prefetch_related("tags").order_by("-created_date")[:3])

        phones_data = []

        for phone in phones:
            phones_data.append({
                "id": phone.id,
                "name": phone.name,
                "image": phone.image.url,
                "context": phone.context,
                "price": phone.price,
                "memory": phone.memory,
                "network": phone.network,
                "tags": [tag.name for tag in phone.tags.all()],
            })

        cache.set("home:latest_phones", phones_data)

    else:
        print("PHONES CACHE HIT")


    # -------------------------
    # Tags
    # -------------------------

    tags_data = cache.get("home:tags")

    if tags_data is None:
        print("TAGS CACHE MISS")

        tags = Tag.objects.all()

        tags_data = [
            {
                "name": tag.name,
            }
            for tag in tags
        ]

        cache.set("home:tags", tags_data)

    else:
        print("TAGS CACHE HIT")


    context = {
        "post": phones_data,
        "tags": tags_data,
    }

    return render(request, "views_html/home.html", context)




def products(request, tag_name=None):

   
    # محصولات بر اساس تگ
    # -------------------------
    post = Tags(tag_name)

    # فیلتر برند
    # -------------------------
    brands = request.GET.getlist('brand')

    if brands:
        post = post.filter(tags__name__in=brands).distinct()

    # فیلتر حافظه داخلی
    # -------------------------
    memories = request.GET.getlist('memory')

    if memories:
        post = post.filter(memory__in=memories)


    # فیلتر شبکه
    # -------------------------
    networks = request.GET.getlist('network')

    if networks:
        post = post.filter(network__in=networks)

    # مرتب سازی
    # -------------------------
    sort = request.GET.get('sort')

    if sort == 'cheap':

        post = post.order_by('price')

    elif sort == 'expensive':

        post = post.order_by('-price')

    elif sort == 'newest':

        post = post.order_by('-created_date')

 
    # -------------------------
    paginator = Paginator(post, 3)

    try:

        page_num = request.GET.get('page')

        post = paginator.get_page(page_num)

    except PageNotAnInteger:

        post = paginator.get_page(1)

    except EmptyPage:

        post = paginator.get_page(1)

    # -------------------------
    context = {
        'post': post,
        'selected_brands': brands,
        'selected_memories': memories,
        'selected_networks': networks,
    }

    return render(request,'views_html/products.html',context)

def brands(request):
    tags = Tag.objects.all()
    context = {'tags':tags}
    return render(request,'views_html/brands.html',context)