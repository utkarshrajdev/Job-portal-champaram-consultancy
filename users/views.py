from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from candidates.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def is_recruiter(user):
    return user.is_staff

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('detail-candidates')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    return render(request, 'users/login.html')

@login_required
@user_passes_test(is_recruiter)
def switch_to_candidate(request):
    request.session['viewing_as_candidate'] = True
    return redirect('detail-candidates')

@login_required
@user_passes_test(is_recruiter)
def switch_to_recruiter(request):
    request.session['viewing_as_candidate'] = False
    return redirect('detail-recruiters')

# Add to your context processor or middleware
def nav_context(request):
    return {
        'viewing_as_candidate': request.session.get('viewing_as_candidate', False) if request.user.is_staff else True
    }

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html',context)


@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'users/account.html', context)

def privacy(request):
    return render(request, 'users/privacy.html')


def terms(request):
    return render(request, 'users/terms.html')


def pricing(request):
    context = {
        'rec_navbar': 1,
    }
    return render(request, 'users/pricing.html', context)
