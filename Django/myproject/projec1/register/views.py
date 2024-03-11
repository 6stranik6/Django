from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import AuthenticationForm, RegistrationForm, User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            # Дополнительные действия после успешной регистрации
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})