from django.shortcuts import render
from django.http import request
from .functions import getweather


def home(request):
    if request.POST.get('cidade') is not None:
        cidade=request.POST.get('cidade')
        values=getweather(cidade)
        if values != "error":
            descricao=[]
            valor=[]
            ID=[]
            for i,j in values.items():
                if i=="ID":
                    ID.append(str(j))
                else:
                    descricao.append(i.upper())
                    valor.append(j)
            return render(request, 'weatherapp/home.html',\
                            {"descricoes":descricao, "valores":valor, "cidades":cidade.upper(), "idcidade":ID})
    else:
        return render(request, 'weatherapp/home.html')
