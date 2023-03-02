from django.shortcuts import render


def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': 'harun',
        }
    else:
        context = {'isim': 'kullanıcı'}
    return render(request, 'home.html', context)
