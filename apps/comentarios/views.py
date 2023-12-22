from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import DeleteView, UpdateView
from apps.noticias.models import Noticia
from .models import Comentario
from django.urls import reverse_lazy
from .forms import Form_Modificacion

def Agregar_Comentario(request,pk):

	texto = request.POST.get('comentario',None)

	noticia = Noticia.objects.get(pk = pk)
	usuario = request.user
	Comentario.objects.create(texto = texto, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticia', kwargs = {'pk':pk}))

class BorrarComentario(DeleteView):
	model = Comentario
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})

class ModificaComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})