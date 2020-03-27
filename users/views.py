from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from .forms import CustomUserCreationForm
from donations.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import admin_required
from .models import User

def home(request):
    return HttpResponse('You are now home!!')


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login-page')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_admin:
        return render(request, 'users/adminprofileview.html')

    else:
        return render(request, 'users/reguserprofile.html')


@login_required
@admin_required
def admin_view(request):
    return HttpResponse("Exclusive test admin page!!!!!!!!!")


@login_required
@admin_required
def usr_view(request):
    user = User.objects.all()
    usr_dict = {'users': user}
    return render(request,template_name='users/usr_view.html', context=usr_dict)