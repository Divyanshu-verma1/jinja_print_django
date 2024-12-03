from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d = {'name': 'Verma', 'age':24}
    return render(request, 'jinja.html', context=d)