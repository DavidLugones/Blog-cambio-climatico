from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Noticia
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia

# Create your views here.
def Home_Noticias(request):

	todas = Noticia.objects.all()

	contexto = {}

	contexto ['noticias'] = todas

	contexto ['fecha'] = '10-12-2023'
	
	return render(request, 'noticias/home_noticias.html', contexto)

class Home_Noticias_clase(ListView):
	model = Noticia
	template_name = 'noticias/home_noticias.html'
	context_object_name = 'noticias'

class Cargar_noticia(CreateView):
	model = Noticia
	template_name = 'noticias/cargar_noticia.html'
	form_class = Formulario_Noticia
	success_url = reverse_lazy('noticias:h_noticias')


def Detalle_noticia(request, pk):
	ctx = {}
	n = Noticia.objects.get(pk = pk)
	ctx['noticia'] = n
	return render(request,'noticias/detalle_noticia.html', ctx)

class Modificar_noticia(UpdateView):
	model = Noticia
	template_name = 'noticias/modificar_noticia.html'
	form_class = Formulario_Modificar_Noticia
	success_url = reverse_lazy('noticias:h_noticias')

class Borrar_noticia(DeleteView):
	model = Noticia
	success_url = reverse_lazy('noticias:h_noticias')


