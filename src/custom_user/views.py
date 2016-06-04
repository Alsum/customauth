from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import LoginForm
from django.contrib import messages
from custom_user.forms import CustomUserCreationForm


def home(request):
    return render(request, "home.html")


def login(request):
    form = LoginForm(request.POST or None)
    btn = "Login"
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=email, password=password)
        auth.login(request, user)
        messages.success(request, "Successfully Logged In. Welcome Back!")
        return HttpResponseRedirect("/")
    context = {
        "form": form,
        "submit_btn": btn,
    }
    return render(request, "login.html", context)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect(reverse('accounts:loggedin'))
    else:
        return HttpResponseRedirect(reverse('accounts:invalid'))


def loggedin(request):
    return render(request, 'loggedin.html',
                  {'user': request.user})


def invalid_login(request):
    return render(request, 'invalid_login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:register_success'))

    else:
        form = CustomUserCreationForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'register.html', args)


def register_success(request):
    return render(request, 'register_success.html')
