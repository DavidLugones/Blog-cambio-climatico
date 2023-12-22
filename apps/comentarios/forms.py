from django import forms
from .models import Comentario

class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)