from django.shortcuts import render

task = ["Read", "Listen", "Watch", "Play", "Chat"]

# Create your views here.
def index(request):
    return render(request, "task/index.html", {
        "task": task

    })

def add(request):
    return render(request, "task/add.html")
        
