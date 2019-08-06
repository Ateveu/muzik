from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect


from .models import Event
from .forms import EventForm


class HomePageView(ListView):
    model = Event
    template_name = 'home.html'

def events_list(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

# class CreateEventView(CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'event/event.html'
#     success_url = reverse_lazy('home')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, "event/event.html", {'form': form})