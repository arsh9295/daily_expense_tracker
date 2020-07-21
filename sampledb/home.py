from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from sampledb.models import detrack
from django.contrib.sessions.models import Session

def homeindex(request):
    #return render(request, 'home.html')
    #username = request.GET.get('text', 'default')
    #password = request.GET.get('password', 'default')
    print(request.method)
    if request.method == 'POST':
        username = request.POST['text']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        #user=str(user)
        #print(user)
        if user is not None:
            auth.login(request, user)
            request.session['is_login'] = True
            return redirect('homemain')
            #return render(request, 'index.html')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'home.html')


def homemain(request):
    if request.method == 'POST':
        expense = detrack()
        expense.datee = request.POST['datee']
        expense.crde = request.POST['crde']
        expense.whrerwhom = request.POST['where']
        expense.howmuch = request.POST['howmuch']
        expense.save()
        #return redirect('list')
        return render(request, 'index.html')
    else:
        if request.session.has_key('is_login'):
            all_data = detrack.objects.all()
            return render(request, 'index.html', {'datalist': all_data})
        else:
            #return render(request, 'home.html')
            return redirect('/')
            #return request('/')


def homesignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        emailid = request.POST['emailid']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=emailid, password=password1)
        user.save();
    else:
        return render(request, 'signup.html')


def logout(request):
    if 'logout' in request.POST:
        print(request.session.has_key('is_login'))
        if request.session.has_key('is_login'):
            request.session.flush()
            #return render(request, 'home.html')
            return redirect('/')
