from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):
    #to arrange the entries by date#
    lists = Entry.objects.order_by('-date_posted')

    return render(request, "lists/index.html", {'lists' : lists})

def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        context = {}
        context['form'] = EntryForm()
        return render(request, "lists/add.html", context)
