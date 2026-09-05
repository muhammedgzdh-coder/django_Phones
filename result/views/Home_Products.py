from django.shortcuts import render , redirect
from result.models.post import Phones
from taggit.models import Tag
from result.selector.tags import Tags
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
     post = Phones.objects.all().order_by('-created_date')[:3]
     tags = Tag.objects.all()
     context = {'post':post,'tags':tags}
     return render(request,'home.html',context)

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

    return render(request,'products.html',context)

def brands(request):
    tags = Tag.objects.all()
    context = {'tags':tags}
    return render(request,'brands.html',context)