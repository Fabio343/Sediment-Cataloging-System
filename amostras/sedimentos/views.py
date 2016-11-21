from django.views import generic
from .models import amostra

class IndexView(generic.ListView):
    template_name ='sedimentos/index.html'
    context_object_name= 'all_amostras'
    
    def get_queryset(self):
        retun amostra.objects.all()
        
        
class DetailView(generic.DetailView):
    model = amostra
    template_name='sedimentos/detail.html'
