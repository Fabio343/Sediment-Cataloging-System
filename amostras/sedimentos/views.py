from django.shortcuts import render, get_object_or_404
from .models import amostra, cidade



def index (request):
    all_amostras=amostra.objects.all()
    return render( request, 'sedimentos/index.html', {'all_amostras': all_amostras})



def detail(request,amostra_id):
    amostra_id = get_object_or_404(amostra, pk=amostra_id)
    return render(request,'sedimentos/detail.html',{'amostra_id':amostra_id})


def destaque (request, amostra_id):
    amostra_id = get_object_or_404(amostra, pk=amostra_id)
    try:
        selected_cidade =amostra_id.cidade_set.get(pk=request.POST['cidade'])
    except(KeyError, cidade.DoesNotExist):
        return render(request,'sedimentos/detail.html',{'amostra_id':amostra_id, 'error_message': "Sem essa informação",})

    else:
        selected_cidade.is_destaque=True
        selected_cidade.save()
        return render(request, 'sedimentos/detail.html', {'amostra_id': amostra_id})



