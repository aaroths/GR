from django.shortcuts import render
from . import views
from django import forms

# Create your views here.

def home(request):

    return render(request,'GR/all.html')

def all(request):

    return render(request,'GR/all.html')

def all2(request):

    return render(request,'GR/all2.html')

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
