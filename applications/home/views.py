from django.shortcuts import render
from django.views.generic import(
    TemplateView,ListView
)

class IndexView(TemplateView) :
    # una vista procesa los datos y renderiza los datos en pantalla 
    # siempre nos pedira un template html
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name ='home/lista.html'
    queryset =['El poder del Jefe','Thinking in Python','Memorias Mzapete']
    context_object_name ='libros'