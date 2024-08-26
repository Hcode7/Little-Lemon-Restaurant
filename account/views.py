from django.shortcuts import render, redirect
from .forms import Registration
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.user = request.user
            new_user.save()
            return redirect('login')
    else:
        form = Registration()
    return render(request, 'registration/register.html', {'form' : form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')