from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, help_text="About You....")
    location = models.CharField(max_length=100)
    theme = models.CharField(max_length=50, choices=[("Theme-1", "1")])

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=100, help_text="Give your skill a name (ex:Baking)")
    about = models.CharField(max_length=300, help_text="Would you care to elaborate?")
    level = models.CharField(max_length=100, choices=[("Beginner", "Beginner"), ("Intermidiate", "Intermidiate"), ("Expert", "Expert"), ("Was born for this", "Was born for this")])

class Social(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="socials")
    platform = models.CharField(max_length=100, choices=[("FaceBook", "FaceBook"), ("Instagram", "Instagram"), ("GitHub", "GitHub")])
    url = models.URLField(help_text="Enter link to platform...")

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=50, help_text="Give your project a name...")
    description = models.TextField(blank=False)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to="media/PingMeUp/projects/", blank=True, null=True)