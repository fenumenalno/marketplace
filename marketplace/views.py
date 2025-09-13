from django.shortcuts import render, redirect
from marketplace import models
from django.contrib.auth import login, authenticate

def main(request):
    tovari = models.Tovari.objects.all()
    otvet = render(request, 'main.html', {'tovari': tovari})
    return otvet

def kartochka(request, tovar_id):
    tovar = models.Tovari.objects.get(id=tovar_id)
    otvet = render(request, 'kartochka.html', {'tovar': tovar})
    return otvet

def korzina(request):
    otvet = render(request, 'korzina.html')
    return otvet

def login_user(request):
    otvet = render(request, 'login.html')
    return otvet

def login_user_post(request):
    password = request.POST['password']
    name = request.POST['username']
    userauth = authenticate(request, password=password, username=name)
    if userauth != None:
        login(request, userauth)
        otvet = redirect('main')
        return otvet
    else:
        oshibka = 'Неправильно введен пароль или имя'
        otvet = render(request, 'login.html', {'oshibka': oshibka})
        return otvet

def logout_user(request):
    otvet = render(request, 'logout.html')
    return otvet

def registration_GET(request):
    otvet = render(request, 'registration.html')
    return otvet

def registration_POST(request):
    password = request.POST['parol']
    name = request.POST['ima']
    email = request.POST['pochta']
    password2 = request.POST['parol2']
    adress = request.POST['adress']
    number = request.POST['number']
    if password != password2:
        otvet = render(request, 'registration.html', {'oshibka': 'пароли не совпадают'})
        return otvet
    imena = models.User.objects.filter(username=name)
    if len(imena) == 1:
        otvet = render(request, 'registration.html', {'oshibka': 'такое имя пользователя уже есть'})
        return otvet
    models.User.objects.create_user(username=name, password=password, email=email, adress=adress, number=number)
    otvet = redirect('main')
    return otvet

def profil(request):
    otvet = render(request, 'profil.html')
    return otvet