from django import forms

class Cursoformulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()