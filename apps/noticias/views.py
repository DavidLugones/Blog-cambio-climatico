from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia
from apps.comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins    import UserPassesTestMixin



def Home_Noticias(request):
    contexto = {}
    cat = Categoria.objects.all()
    contexto['categorias'] = cat

    filtro = request.GET.get('categoria', None)
    orden = request.GET.get('orden', None)

    if not filtro or filtro == '0':
        todas = Noticia.objects.all()
    else:
        categoria_seleccionada = Categoria.objects.get(pk=filtro)
        todas = Noticia.objects.filter(categoria=categoria_seleccionada)

    if orden == "asc":
        todas = todas.order_by('creado')
    elif orden == 'dsc':
        todas = todas.order_by('-creado')

    contexto['noticias'] = todas
    return render(request, 'noticias/home_noticias.html', contexto)

class Home_Noticias_clase(ListView):
    model = Noticia
    template_name = 'noticias/home_noticias.html'
    context_object_name = 'noticias'

class Cargar_noticia(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:h_noticias')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.usuario = self.request.user
        return super(Cargar_noticia, self).form_valid(form)

class Modificar_noticia(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Noticia
    template_name = 'noticias/modificar_noticia.html'
    form_class = Formulario_Modificar_Noticia
    success_url = reverse_lazy('noticias:h_noticias')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

class Borrar_noticia(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:h_noticias')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

def Detalle_noticia(request, pk):
    ctx = {}
    n = Noticia.objects.get(pk=pk)
    ctx['noticia'] = n

    com = Comentario.objects.filter(noticia=n)
    ctx['comentarios'] = com
    return render(request, 'noticias/detalle_noticia.html', ctx)