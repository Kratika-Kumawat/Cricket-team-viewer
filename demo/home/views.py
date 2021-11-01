from .forms import TeamForm, Teams
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Teams, BaseUser
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login successfully')
            return redirect('/main')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('/')
    else:
        messages.info(request, 'Please login First')
        return render(request, 'index1.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = BaseUser.objects.create_user(
            username=username, first_name=firstname, last_name=lastname, email=email, password=password)
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        user.gender = request.POST['gender']
        user.dob = request.POST['dob']
        user.save()
        messages.success(request, "signup successfully")
        return redirect("/")
    else:
        return render(request, 'signup.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        team = Teams.objects.all()
        return render(request, 'index.html', {'team': team})
    else:
        messages.info(request, "login failed")
        return redirect("/")


def addteam(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Added Team Successfully!")
            return redirect("/main")
        else:
            team = TeamForm()
            messages.info(request, "Invalid Data!")
            return render(request, 'addteam.html', {'team': team})
    else:
        team = TeamForm()
        return render(request, 'addteam.html', {'team': team})


def delete(request):
    id = request.GET['id']
    id = int(id)
    t = Teams()
    t.id = id
    t.delete()
    messages.success(request, "Deleted Team Successfully!")
    return redirect("/main")


def logout(request):
    auth.logout(request)
    messages.info(request, "Logout Successfully")
    return redirect("/")


def main(request):
    team = Teams.objects.all()
    return render(request, 'index.html', {'team': team})


def update(request):
    id = request.GET['id']
    id = int(id)
    obj = get_object_or_404(Teams, id=id)
    form = TeamForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Team Updated Successfully!")
        return redirect("/main")
    else:
        return render(request, 'update.html', {'info': form})
