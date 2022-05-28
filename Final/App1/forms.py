from django import forms


class Profesor_form(forms.Form):
    name = forms.CharField(max_length=20, min_length=3, label="name")
    born = forms.DateField(label='born',widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    email = forms.EmailField(label='email')

class Alumno_form(forms.Form):
    name = forms.CharField(max_length=20, min_length=3, label="name")
    born = forms.DateField(label='born',widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    email = forms.EmailField(label='email')

class Curso_form(forms.Form):
    curso = forms.CharField(max_length=20, min_length=3, label="curso")
    camada = forms.IntegerField(label='camada')