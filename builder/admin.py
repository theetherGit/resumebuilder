from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import (Type, ResumeTemplate, PersonProfileImage, PersonDetail, PersonCareerObjective,
                     PersonWorkExperience, PersonAcademicQualification, PersonCertificationCourse,
                     PersonProject, PersonPosition, PersonSkill, PersonHobbie, PersonKnownLanguage)
User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'is_admin', 'is_staff', 'is_pro', 'user_sid', 'user_cid']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_pro')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['resume_name', 'resume_uid', 'resume_type']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'name', 'email', 'contact']


class PersonProfileImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'image']


class PersonCareerObjectiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'aim']


class PersonWorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'name', 'position', 'duration']


class PersonAcademicQualificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'qualification', 'institution', 'passed']


class PersonCertificationCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'name', 'institution', 'year']


class PersonProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'name']


class PersonPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'name', 'place', 'year']


class PersonSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'skill']


class PersonHobbieAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'hobby']


class PersonKnownLanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'person', 'lang']


admin.site.register(User, UserAdmin)
admin.site.register(ResumeTemplate, ResumeAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(PersonDetail, DetailsAdmin)
admin.site.register(PersonProfileImage, PersonProfileImageAdmin)
admin.site.register(PersonCareerObjective, PersonCareerObjectiveAdmin)
admin.site.register(PersonWorkExperience, PersonWorkExperienceAdmin)
admin.site.register(PersonAcademicQualification, PersonAcademicQualificationAdmin)
admin.site.register(PersonCertificationCourse, PersonCertificationCourseAdmin)
admin.site.register(PersonProject, PersonProjectAdmin)
admin.site.register(PersonPosition, PersonPositionAdmin)
admin.site.register(PersonSkill, PersonSkillAdmin)
admin.site.register(PersonHobbie, PersonHobbieAdmin)
admin.site.register(PersonKnownLanguage, PersonKnownLanguageAdmin)
