from result.forms import FormComment


def Save_Comment(request, post):

    form = FormComment(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.save()
        return form, True

    return form, False