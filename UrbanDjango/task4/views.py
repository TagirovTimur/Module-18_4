from django.shortcuts import render


def platform(request):
    return render(request, 'fourth_task/platform.html')


def games_store(request):
    context = {
        'name_game': ['Warhammer Quest: Cursed City', 'Древний Ужас: Разрушенные города', 'Эверделл'],
    }
    return render(request, 'fourth_task/games.html', context)


def cart_of_store(request):
    return render(request, 'fourth_task/cart.html')