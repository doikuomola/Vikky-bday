from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from birthday.forms import ImageForm

from .models import BirthdayDate, Image, Wish


def homeView(request):
    date = BirthdayDate.objects.all()
    wishes_count = Wish.objects.all().count()
    context = {
        "date": date,
        "wishes_count":wishes_count,
    }
    return render(request, 'birthday/home.html', context)


def dashboard(request):

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
        
    return render(request, 'birthday/dashboard.html', {'form': form})


def live(request):
    images = Image.objects.all().order_by('-createAt')
    context = {'images': images}
    return render(request, 'birthday/live.html', context)


def createwish(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        new_wish = Wish(name=name, phone_number=phone_number, message=message)
        new_wish.save()
        return redirect('home')


def wishes(request):
    wishes = Wish.objects.all().order_by('-createAt')
    context = {'wishes': wishes}
    return render(request, 'birthday/wishes.html', context)