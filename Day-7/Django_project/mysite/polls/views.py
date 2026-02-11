from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the index page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def about(request):
    return HttpResponse("This is the about page")