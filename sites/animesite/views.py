from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': "Алексей"}
    return render(request, 'index.html', context)

def anime(request):
    return render(request, 'anime.html')

def wathinganime(request):
    return render(request, 'wathinganime.html')