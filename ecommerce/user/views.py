from django.shortcuts import render, HttpResponse
from administrator.forms import *
from administrator.models import *

# Create your views here.
def index(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, "user/about.html")

def contact(request):
    context = {}
    if request.method == "GET":
        context['form'] = ContactForm()
        return render(request, "user/contact.html", context)
    elif request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thank you for your message.")
        else:
            context['form'] = form
            return render(request, "user/contact.html", context)

def seed_user(request):
    from faker import Faker
    from faker.providers import internet
    fake = Faker()
    users = []
    for i in range(100):
        user = User()
        user.first_name = fake.name().split(' ')[0]
        user.last_name = fake.name().split(' ')[1]
        user.email = fake.ascii_free_email()
        user.set_password(fake.password())
        users.append(user)
    User.objects.bulk_create(users)
    return HttpResponse("Seeded 100 users.")