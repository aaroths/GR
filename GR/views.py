from django.shortcuts import render
from django.shortcuts import redirect
from . import views
from django import forms
from .forms import FavoriteForm
from .models import Favorite,Intervention

# Create your views here.

def home(request):
    user = request.user
    interventions=Intervention.objects.all().values().order_by('displayorder')

    if request.method == "POST":
        form = FavoriteForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            favorite = form.save(commit=False)
            favorite.author = request.user
            if Favorite.objects.filter(author=user,fav=data['fav']).count()!=0:
                Favorite.objects.filter(author=user,fav=data['fav']).update(toggle='True')
            else:
                favorite.toggle = "True"
                favorite.save()

            return redirect('home')
    else:
        form = FavoriteForm()

    return render(request,'GR/content.html', {'form':form,'interventions':interventions})


#def all(request):

#    return render(request,'GR/all.html')

def homealt (request):

    return render(request,'GR/all3.html')

def all2(request):
    user = request.user
    interventions=Intervention.objects.all().values().order_by('displayorder')

    if request.method == "POST":
        form = FavoriteForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            favorite = form.save(commit=False)
            favorite.author = request.user
            if Favorite.objects.filter(author=user,fav=data['fav']).count()!=0:
                Favorite.objects.filter(author=user,fav=data['fav']).update(toggle='True')
                favorite.save()
            else:
                favorite.toggle = "True"
                favorite.save()

            return redirect('favorite',pk=favorite.pk)
    else:
        form = FavoriteForm()

    return render(request,'GR/all2.html', {'form':form,'interventions':interventions})

def favorite (request):
    user = request.user
    interventions=Intervention.objects.all().values().order_by('displayorder')
    favorites=Favorite.objects.filter(author=user,toggle=True).values('fav_id')
    listfavorites=list(favorites)
    newlist = []

    for favorite in favorites:
        for intervention in interventions:
            if str(favorite['fav_id']) == str(intervention['id']):
                newlist.append(intervention)

    if request.method == "POST":
        form = FavoriteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            favorite = form.save(commit=False)
            favorite.author = request.user
            Favorite.objects.filter(author=user,fav=data['fav']).update(toggle='False')

        else:
            form = FavoriteForm()
        return redirect('favorite')

    return render(request,'GR/favorite.html',{'interventions':interventions,'favorites':favorites,'listfavorites':listfavorites,'newlist':newlist})


def about(request):

    return render(request,'GR/about.html')

def resilience (request):

    return render(request,'GR/resilience.html')

def emergency (request):

    return render(request,'GR/emergency.html')


#Tools
def threePs(request):

    return render(request,'GR/tool/threePs.html')

def shutdown(request):

    return render(request,'GR/tool/shutdown.html')

def reset(request):

    return render(request,'GR/tool/reset.html')

def littlewins(request):

    return render(request,'GR/tool/littlewins.html')

def zero(request):

    return render(request,'GR/tool/zero.html')

def keystone(request):

    return render(request,'GR/tool/keystone.html')

def journal(request):

    return render(request,'GR/tool/journal.html')

def chain(request):

    return render(request,'GR/tool/chain.html')

def arrow(request):

    return render(request,'GR/tool/arrow.html')

#activities
def goal(request):

    return render(request,'GR/activity/goal.html')

def label(request):

    return render(request,'GR/activity/label.html')

def ministry(request):

    return render(request,'GR/activity/ministry.html')

def space(request):

    return render(request,'GR/activity/space.html')

def threeselves(request):

    return render(request,'GR/activity/threeselves.html')

def universes(request):

    return render(request,'GR/activity/universes.html')

#Mindsets
def vulnerability(request):

    return render(request,'GR/mindset/vulnerability.html')

def mindfulness(request):

    return render(request,'GR/mindset/mindfulness.html')

def growth(request):

    return render(request,'GR/mindset/growth.html')

def design(request):

    return render(request,'GR/mindset/design.html')

def curiosity(request):

    return render(request,'GR/mindset/curiosity.html')

def compassion(request):

    return render(request,'GR/mindset/compassion.html')
