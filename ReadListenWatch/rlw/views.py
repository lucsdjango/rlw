from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from rlw.models import *


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
	
	
def text(request):
	group = Condition.objects.all().order_by('?')[0]
	request.session['group'] = group.name
	txt=Text.objects.filter(description="text1",)[0]
	template = loader.get_template('text.html')
	context = RequestContext(request, 
		{'txt':  txt,
		'group': request.session['group']})
	
	return HttpResponse(template.render(context))
	
