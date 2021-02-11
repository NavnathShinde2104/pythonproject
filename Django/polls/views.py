from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hey Hello, world. You're at the polls index.")
