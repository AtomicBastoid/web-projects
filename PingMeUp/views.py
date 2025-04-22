from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProfileForm, SkillFormSet, ProjectFormSet, SocialFormSet

# Index View
def index(request):
    return render(request, "PingMeUp/index.html")

# Create Profile View
def create(request):
    if request.method == "POST":

        return HttpResponse("Forms Recieved!")
    
    else:
        profile = ProfileForm()
        socials = SocialFormSet()
        skills = SkillFormSet()
        projects = ProjectFormSet()

    return render(request, "PingMeUp/create.html", {
        "profile" : profile,
        "socials" : socials,
        "skills" : skills,
        "projects" : projects

    })


