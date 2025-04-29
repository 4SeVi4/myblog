from django.http import HttpResponse

def home(request):
    return HttpResponse("Вітаю на сайті!")
