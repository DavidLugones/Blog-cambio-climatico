from django.shortcuts import render

# Create your views here.
def Home_Informate(request):
	
	return render(request, 'informate/home_informate.html')
def Home_Informate(request):
    context = {
        'image': '{{ n.imagen.url }}'  # Asegúrate de que esta ruta sea accesible
    }
    return render(request, 'informate/home_informate.html', context)
