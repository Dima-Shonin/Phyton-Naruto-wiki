from django.shortcuts import render
from . models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
import random
from rest_framework import generics
from . serializers import *



def index(request):
    rand = random.randint(1, 5)
    context = {
        'technic': Technics.objects.get(pk=rand),
    }
    return render(request, 'wiki/index.html',context)


@login_required
def Villages(request):
    context = {
        'villages': Village.objects.order_by('id'),
    }
    return render(request, 'wiki/Villages.html',context)


@login_required
def Village_detail(request,pk):
    context = {
        'village': Village.objects.get(pk=pk),
    }
    return render(request, 'wiki/Village_detail.html', context)


@login_required
def Shinobies(request):
    context = {
        'shinobies': Shinobi.objects.order_by('id'),
    }
    return render(request, 'wiki/Shinobies.html',context)


@login_required
def Shinobi_detail(request,pk):
    context = {
        'shinobi': Shinobi.objects.get(pk=pk),
    }
    return render(request, 'wiki/Shinobi_detail.html', context)


@login_required
def Technicss(request):
    context = {
        'technics': Technics.objects.order_by('id'),
    }
    return render(request, 'wiki/Technics.html',context)


@login_required
def Technic_detail(request,pk):
    context = {
        'technic': Technics.objects.get(pk=pk),
    }
    return render(request, 'wiki/Technic_detail.html', context)


@login_required
def Battles(request):
    context = {
        'battles': Battle.objects.order_by('id'),
    }
    return render(request, 'wiki/Battles.html',context)


@login_required
def Battle_detail(request,pk):
    context = {
        'battle': Battle.objects.get(pk=pk),
    }
    return render(request, 'wiki/Battle_detail.html', context)


class ShinobiListAPIView(generics.ListAPIView):
    queryset = Shinobi.objects.order_by('id')
    serializer_class = ShinobiSerializer1

