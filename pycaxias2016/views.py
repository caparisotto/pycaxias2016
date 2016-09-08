# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import os,sys,psycopg2.extras,time

# Create your views here.

def inicial(request):
	proximo = "/slide2/"
        return render_to_response("capa.html",{'proximo': proximo})

def slide2(request):
	number = 2
	anterior = "/"
	proximo = "/slide3/"
        return render_to_response("slide2.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide3(request):
	number = 3
	anterior = "/slide2/"
	proximo = "/slide4/"
        return render_to_response("slide3.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide4(request):
	number = 4
	anterior = "/slide3/"
	proximo = "/slide5/"
        return render_to_response("slide4.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide5(request):
	number = 5
	anterior = "/slide4/"
	proximo = "/slide6/"
        return render_to_response("slide5.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide6(request):
	number = 6
	anterior = "/slide5/"
	proximo = "/slide7/"
        return render_to_response("slide6.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide7(request):
	number = 7
	anterior = "/slide6/"
	proximo = "/slide8/"
        return render_to_response("slide7.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide8(request):
	number = 8
	anterior = "/slide7/"
	proximo = "/slide9/"
        return render_to_response("slide8.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide9(request):
	number = 9
	anterior = "/slide8/"
	proximo = "/slide10/"
        return render_to_response("slide9.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide10(request):
	number = 10
	anterior = "/slide9/"
	proximo = "/slide11/"
        return render_to_response("slide10.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def slide11(request):
	number = 11
	anterior = "/slide10/"
	proximo = "/end/"
        return render_to_response("slide11.html",{'number': number, 'anterior': anterior, 'proximo': proximo})

def final(request):
	anterior = "/slide11/"
        return render_to_response("ultimo.html",{'anterior': anterior})
