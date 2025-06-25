from django.contrib import admin
from .models import Profile, Skill, Social, Project

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class SocialInline(admin.TabularInline):
    model = Social
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "middle_name", "last_name", "location", "theme")
    search_fields = ("first_name", "middle_name", "last_name", "location", "user__username")
    list_filter = ("theme",)
    inlines = [SkillInline, SocialInline, ProjectInline]
