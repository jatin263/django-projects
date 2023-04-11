from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def Home(request):
    name=['Jatin',"saurabh"]
    return JsonResponse(name,safe=False)