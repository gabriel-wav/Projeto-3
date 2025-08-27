from django.shortcuts import render, get_object_or_404
from .models import Foto

# Create your views here.
def home(request):
    return render(request, 'fotos/home.html')

def foto_detail(request, id):
    foto = get_object_or_404(Foto, id=id)
    context = {'foto': foto}
    return render(request, 'fotos/foto_detail.html', context)

def pesquisar_fotos(request): 
    query = request.GET.get("q")
    resultados = []
    
    if query:
        resultados = Foto.objects.filter(title__icontains=query)
        
    context = {'query': query, 'resultados': resultados}
    return render(request, 'fotos/pesquisar_fotos.html', context)