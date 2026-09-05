from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme 
# Create your views here.

def login_view(request):

    if request.user.is_authenticated:
        return redirect('result:home')
    if request.method == 'POST':
        
        form = AuthenticationForm(request=request,data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect('result:home')

        else:
            print(form.errors)

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(
        request,'login.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('result:home')


def signup(request):
    if request.user.is_authenticated:
        return redirect('result:home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Accounts:login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)   

