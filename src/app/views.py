from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

# def home_view(request):
    # print(request.META)
    # return HttpResponse("Hello World!")

def home_view(request):
    context = {
        "first_name": "Ata",
        "last_name": "Dev"
    }
    return render(request, "app/home.html", context)
