from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import ProfileForm, SkillFormSet, ProjectFormSet, SocialFormSet
from django.contrib.auth.models import User
from .models import Profile

# ----------------------------------------------------------------
# Making some functions that will help in views
def get_or_create_profile(user):
    """
    Checks if the user has a profile object 
    if has:
    --> return profile
    else:
    --> creates profile and then returns it
    """
    profile, _created = Profile.objects.get_or_create(user=user)
    return profile

# ----------------------------------------------------------------

# --------------------Index View----------------------------------
def index(request):
    return render(request, "PingMeUp/index.html")

# -------------------Edit View------------------------------------
@login_required
def edit(request):
    if request.method == "POST":

        return HttpResponse("Forms Recieved!")
    
    else:
        profile = ProfileForm(instance=get_or_create_profile(request.user))
        socials = SocialFormSet(instance=get_or_create_profile(request.user), prefix="socials")
        skills = SkillFormSet(instance=get_or_create_profile(request.user), prefix='skills')
        projects = ProjectFormSet(instance=get_or_create_profile(request.user),prefix="projects")

    return render(request, "PingMeUp/edit.html", {
        "profile" : profile,
        "socials" : socials,
        "skills" : skills,
        "projects" : projects

    })

#---------------------Ajax Views----------------------------------
@login_required
@require_POST
def save_profile_ajax(request):
    profile_obj = get_or_create_profile(request.user)
    form = ProfileForm(request.POST, instance=profile_obj)
    form.user = request.user
    if form.is_valid():
        form.save()
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False, "errors": form.errors}, status=400)
    
@login_required
@require_POST
def save_skills_ajax(request):
    fs = SkillFormSet(request.POST, instance=get_or_create_profile(request.user), prefix="skills")
    if fs.is_valid():
        fs.save()
        return JsonResponse({"ok": True, "msg": "Skills Saved"})
    return JsonResponse({"ok": False, "errors": fs.errors}, status=400)

@login_required
@require_POST
def save_projects_ajax(request):
    fs = ProjectFormSet(request.POST, instance=get_or_create_profile(request.user), prefix="projects")
    if fs.is_valid():
        fs.save()
        return JsonResponse({"ok": True, "msg": "Projects Saved"})
    return JsonResponse({"ok": False, "errors": fs.errors}, status=400)

@login_required
@require_POST
def save_socials_ajax(request):
    fs = SocialFormSet(request.POST, instance=get_or_create_profile(request.user), prefix="socials")
    if fs.is_valid():
        fs.save()
        return JsonResponse({"ok": True, "msg": "Projects Saved"})
    return JsonResponse({"ok": False, "errors": fs.errors}, status=400)

@login_required
def test(request):
    return render(request, "PingMeUp/test.html", {
        "profile": ProfileForm(instance=get_or_create_profile(request.user)),
        "skills": SkillFormSet(instance=get_or_create_profile(request.user), prefix="socials")
    })