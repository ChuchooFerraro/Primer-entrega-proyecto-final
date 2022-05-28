from django import forms


class Profesor_form(forms.Form):
    name = forms.CharField(max_length=20, min_length=3, label='Nombre')
    #born = forms.DateField(label='Nacimiento')
    email = forms.EmailField(label='Email')