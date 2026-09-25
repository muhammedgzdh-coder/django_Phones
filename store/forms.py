from django import forms
from .models import Comment
from captcha.fields import CaptchaField

class FormComment(forms.ModelForm):

    captcha = CaptchaField(label =False)
    class Meta:
        model = Comment
        fields = ['message']