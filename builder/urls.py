from django.urls import path
from .views import (home, signup, loginuser, logoutuser, dashboard, resumetemplate, typeadd,
                    personaldetails, academic, workex, extra, personalform, careerobjective, workexperience,
                    academicqualification, certificatecourses, projects, positionsres, skillsets, hobbies,
                    knownlanguage, ViewPDF, texview, test123)


urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('login/', loginuser, name="login"),
    path('logout/', logoutuser, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('extra/', extra, name="extra"),
    path('academic/', academic, name="academic"),
    path('workexperience/', workex, name="workex"),
    path('personaldetails/', personaldetails, name="personaldetails"),
    path('addpersonaldetails/', personalform, name="personaldetailsform"),
    path('addcareerobjective/', careerobjective, name="careerobjectiveform"),
    path('addworkexperience/', workexperience, name="workexperienceform"),
    path('addcertificatecourses/', certificatecourses, name="certificatecoursesform"),
    path('addacademicqualification/', academicqualification, name="academicqualificationfrom"),
    path('addprojects/', projects, name="projectsform"),
    path('addpositions/', positionsres, name="positionsresform"),
    path('addskills/', skillsets, name="skillsetsform"),
    path('addhobbies/', hobbies, name="hobbiesform"),
    path('addlanguage/', knownlanguage, name="knownlanguageform"),
    path('resume/', resumetemplate, name="resume"),
    path('texresume/', texview, name="tex"),
    path('test/', test123, name="test"),
    path('resumepdf/', ViewPDF.as_view(), name="yourresume"),
    path('type/', typeadd, name="type"),
]
