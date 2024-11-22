from os.path import exists

from django.shortcuts import render, redirect

from vacateapp.models import Contact, Bookspace,User


# Create your views here.
def starter(request):
    return render(request,'starter-page.html')
def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request ,'service.html')
def books(request):
    if request.method == "POST":
        myspace = Bookspace(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            date = request.POST['date'],
            time = request.POST['time'],
            location = request.POST['location'],
            message = request.POST['message'],
        )
        myspace.save()
        return redirect('/book')
    else:
        return render(request, 'bookspace.html')
def index(request):
    if request.method == "POST":
        if User.objects.filter(



                email = request.POST['email'],
                password = request.POST['password'],

               ).exists():
                return render(request, 'index.html')
        else:

            return redirect('/login')
    else:
        return render(request,'login.html')


def login(request):
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        myuser = User(
            name = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        myuser.save()

        return redirect('/login')
    else:
        return render(request,'registration.html')