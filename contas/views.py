from django.shortcuts import render
from .models import Transacao
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1','t2','t3']
    data['now']= datetime.datetime.now()
    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)