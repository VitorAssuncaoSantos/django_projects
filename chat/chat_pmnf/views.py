from django.shortcuts import render, redirect
from .forms import MensagemForm
from .models import Sala, Messagem
# Create your views here.

def index(request):
    grupos = request.user.groups.all()

    context = {
        'salas': Sala.objects.filter(grupo__in = grupos),
        'salas_user': Sala.objects.filter(participante=request.user)
    }
    return render(request, "index.html", context)

    
def sala(request, id): 
    try:
        sala=Sala.objects.get(id=id)
    except:
        return redirect('/')

    form=MensagemForm(initial={'user': request.user.id, 'sala': sala})
    if request.method == 'POST':
        form=MensagemForm(request.POST)
        if form.is_valid():
            mensagem=form.save(commit=False)
            mensagem.sala=sala
            mensagem.user=request.user
            mensagem.save()
            form=MensagemForm(initial={'user': request.user.id, 'sala': sala})

    context = {
        'id': str(id),
        'nome_da_sala': 'Sala '+str(id),
        'form': form,
        'mensagens': Messagem.objects.filter(sala=id)

    }
    return render(request, "sala.html", context)


def get_mensagens(request, sala): 
    context = {
        "mensagens": Messagem.objects.filter(sala = sala)
    }
    return render(request, "mensagens.html", context)