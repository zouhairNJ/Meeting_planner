from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.forms import modelform_factory

from .models import Meeting,Room
from .forms import MeetingForm
# Create your views here.

def welcome(request):
    return render(request,"meetings/welcome.html",{
        "rooms":Room.objects.all(),
        "meetings": Meeting.objects.all()

    })

def detail (request,id):
    meeting=get_object_or_404(Meeting,pk=id)
    return render (request,"meetings/detail.html", {"meeting" : meeting})

def room(request):
   # room=get_object_or_404(Room.name)
    return render(request,"meetings/rooms.html",
                  {"rooms":Room.objects.all()}
                   )

#MeetingForm=modelform_factory(Meeting,exclude=[])

def new(request):
    if request.method =="POST":
        form=MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=MeetingForm()
    return render (request, "meetings/new.html", {"form": form})




