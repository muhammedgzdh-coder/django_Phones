from django.db import models
from django.contrib.auth.models import User
from .post import Phones

class Comment(models.Model):

    post = models.ForeignKey(Phones,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    message = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author} - {self.post}'