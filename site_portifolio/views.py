from django.shortcuts import render

# Create your views here.
def home(request):
    nome= 'Homem de ferro'
    conhecimento= ['Git', 'JavaScripts', 'Python', 'Django']

    return render(request, 'index.html', {'conhecimento':conhecimento, 'nome': nome})
