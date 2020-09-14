from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Coffe

# Create your views here.

def index(request):
  return render(request, 'index.html')

@login_required(login_url='/')
def coffees(request):
  coffees = Coffe.objects.all()
  return render(request, 'coffees.html', {'coffees': coffees})

def create(request):
  if(request.method == 'POST'):
    name = request.POST['name']
    category = request.POST['category']
    items = request.POST.getlist('ingredient')
    coffee = Coffe.objects.create(name = name, category = category, items = items)
    coffee.save()
    messages.info(request, 'Your order is successfuly send')
    return redirect('/')
  else:
    return render(request, 'create.html')

@login_required(login_url='/')
def delete_coffee(request, id):
  coffee = Coffe.objects.get(id = id)
  coffee.delete()
  return redirect('/coffees')


@login_required(login_url='/')
def view(request, id):
  coffee = Coffe.objects.get(id = id)
  return render(request, 'view.html', {'coffee': coffee})

def login_view(request):
  if(request.method == 'POST'):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username = username, password = password)
    if user is not None:
      auth.login(request, user)
      return redirect('/coffees')
    else:
      messages.info(request, 'Information is not correct')
      return redirect('/login')
  else:
    return render(request, 'login.html')

@login_required(login_url='/')
def logout_user(request):
  auth.logout(request)
  return redirect('/')
