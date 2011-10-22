# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from models import *
#from forms import *
from django.core import serializers
from django.utils import simplejson
from parse import *
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, Context

#secure all evals!

def GiveGetCode(request):
     if request.is_ajax():
          if request.method == "POST":
               #return HttpResponse(data['code'])
               parsed = HACK(request.POST["code"])
               thiscode = Code(rawcode = request.POST["code"],
                               serialcode = parsed)
               thiscode.save()
               return HttpResponse(simplejson.dumps({"ID":thiscode.id, "parsed":parsed}), 'application/json')
          
          if request.method == "GET":
               thiscode = Code.objects.get(id=request.GET["ID"])
               return HttpResponse(simplejson.dumps({"raw":thiscode.rawcode, "parsed":HACK(thiscode.rawcode)}), 'application/json')


def DisplayCode(request, ID):
     return render_to_response('results.html', context_instance=RequestContext(request))
     
