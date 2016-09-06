# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import os,sys,psycopg2.extras,time

# Create your views here.

def inicial(request):
	titulo = "Usando Python para ser um Sysadmin Melhor"
	proximo = "/slide2/"
        return render_to_response("capa.html",{'titulo': titulo, 'proximo': proximo})

def slide2(request):
	number = 2
	anterior = "/"
	proximo = "/slide3/"
	titulo = "Pilot"
        return render_to_response("slide2.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide3(request):
	number = 3
	anterior = "/slide2/"
	proximo = "/slide4/"
	titulo = "MBSafe"
        return render_to_response("slide3.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide4(request):
	number = 4
	anterior = "/slide3/"
	proximo = "/slide5/"
	titulo = "MBSafe"
        return render_to_response("slide4.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide5(request):
	number = 5
	anterior = "/slide4/"
	proximo = "/slide6/"
	titulo = "MBSafe"
        return render_to_response("slide5.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide6(request):
	number = 6
	anterior = "/slide5/"
	proximo = "/slide7/"
	titulo = "MBSafe"
        return render_to_response("slide6.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide7(request):
	number = 7
	anterior = "/slide6/"
	proximo = "/slide8/"
	titulo = "MBSafe"
        return render_to_response("slide7.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide8(request):
	number = 8
	anterior = "/slide7/"
	proximo = "/slide9/"
	titulo = "Outras Aplicações"
        return render_to_response("slide8.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide9(request):
	number = 9
	anterior = "/slide8/"
	proximo = "/end/"
	titulo = "Novas Estratégias"
        return render_to_response("slide9.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def final(request):
	titulo = "Perguntas?"
	anterior = "/slide13/"
        return render_to_response("ultimo.html",{'titulo': titulo, 'anterior': anterior})
