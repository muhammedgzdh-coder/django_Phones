from django.shortcuts import render , redirect
from result.models.post import Phones
from django.shortcuts import get_object_or_404
from result.services.comment import Save_Comment
from django.contrib import messages
from result.forms import FormComment
from result.models import Comment
from taggit.models import Tag
from result.selector.tags import Tags
from django.db.models import Q


def product_detail(request, id):

    post = get_object_or_404(Phones, id=id)

    if request.method == 'POST' and request.user.is_authenticated:
        form, status = Save_Comment(request, post)
        
        if status:
            messages.success(request,'نظر شما با موفقیت ثبت شد؛ اگر مورد تایید قرار بگیرد نمایش داده خواهد شد')
        else:
            messages.error(request,'نظر شما ثبت نشد؛ لطفاً دوباره امتحان کنید')

    else:

        form = FormComment()

    comment = Comment.objects.filter(post=post,is_approved=True)
    context = {'post': post,'comment': comment,'form': form,}
    return render(request,'product_detail.html',context)




def Search_Phones(request):

    post = Phones.objects.all()
    if request.method == 'GET':
        if result := request.GET.get('s'):
            query = Q()
            for field in Phones._meta.get_fields():

                if field.get_internal_type() in ['CharField', 'TextField']:
                    query |= Q(**{f'{field.name}__icontains': result})

            post = post.filter(query)


    context = {'post': post}

    return render(request, 'products.html', context)

             