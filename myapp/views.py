from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Vikingos</h1>")


def about(request):
    return HttpResponse("<h1>About Vikingos</h1>")
