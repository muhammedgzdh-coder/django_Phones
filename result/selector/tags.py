from result.models import Phones


def Tags(tag_name=None):

    post = Phones.objects.all()

    if tag_name:
        post = post.filter(tags__name=tag_name)

    return post
