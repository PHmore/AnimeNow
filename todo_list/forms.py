# forms.py

from django import forms
from animes.models import Episodio

class MarcarForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = []  # Nenhum campo será exibido no formulário, 
        # pois não haverá entrada do usuário para as alterações feitas

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.assistido = not instance.assistido
        if commit:
            instance.save()
        return instance
