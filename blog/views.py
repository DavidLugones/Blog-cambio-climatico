from django.shortcuts import render
from django.views import View

def Home(request):

	return render(request,'home.html')

class Registro(View):
    def get(self, request):
        return render(request, 'registro.html')

