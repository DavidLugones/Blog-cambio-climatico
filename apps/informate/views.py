from django.shortcuts import render

# Create your views here.
def Home_Informate(request):
	
	return render(request, 'informate/home_informate.html')