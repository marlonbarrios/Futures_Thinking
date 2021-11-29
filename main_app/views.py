from django.db.models.fields import SlugField
from django.shortcuts import render
from .models import UserEntries
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request, pk):
    entry = UserEntries.objects.get(id=pk)
    return render(request, 'profile/detail.html',{
        'entry': entry
    })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # handle the creation of a new user
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # this creates a session entry in the database
            login(request, user)
            # # and it persists that session sitewide until the user logs out
            return redirect('feed')
        else:
            error_message = 'invalid data - please try again'
    # this is for GET requests, assuming our user clicked on "signup" from the navbar
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class Feed(ListView):
    queryset = UserEntries.objects.order_by('-date')
    model = UserEntries
    template_name = 'feed.html'

class Profile(LoginRequiredMixin, ListView):
    model = UserEntries
    template_name = 'profile/index.html'

    def get_queryset(self):
        queryset = UserEntries.objects.filter(user=self.request.user)
        return queryset

class EntryCreate(LoginRequiredMixin, CreateView):
    model = UserEntries
    fields = ('title', 'entry', 'img', 'video' )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

  

class EntryUpdate(LoginRequiredMixin, UpdateView):
  model = UserEntries
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['title', 'entry', 'img', 'video' ]

class EntryDelete(LoginRequiredMixin, DeleteView):
    model = UserEntries
    success_url = '/profile/'

    def get_queryset(self):
        queryset = UserEntries.objects.filter(user=self.request.user)
        return queryset
  
  