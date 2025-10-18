from django.shortcuts import render


def welcome(request, name):
    '''
    Simple example to validate Django environment
    '''
    context = {
        'name': name
    }
    return render(request, 'index.html', context)
