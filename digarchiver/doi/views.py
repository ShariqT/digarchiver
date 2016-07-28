from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'doi/index.html')



def process(request):
	return HttpResponse("processing the zip file")


def details(request):
	return HttpResponse("this is the project details")


def processdetails(request):
	return HttpResponse("this is the process details")


def share(request):
	return HttpResponse("this is the share page")