from django.forms import ModelForm, inlineformset_factory
from .models import Profile, Skill, Social, Project


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "middle_name", "last_name", "bio", "location", "theme"]
        labels = {
            "first_name" : "First Name",
            "middle_name" : "Middle Name",
            "last_name" : "Last Name",
            "bio" : "Bio",
            "locaation" : "Country/Origin",
            "theme" : "Theme"
        }

ProjectFormSet = inlineformset_factory(Profile, Project, fields=['title', 'description'], extra=1, can_delete=True)
SkillFormSet = inlineformset_factory(Profile, Skill, fields=['name', 'level'], extra=1, can_delete=True)
SocialFormSet = inlineformset_factory(Profile, Social, fields=['platform', "url"], extra=1, can_delete=True)