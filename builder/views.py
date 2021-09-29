from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .validator import passvalid, isEmailAddressValid, uservalidator
from .models import (Type, ResumeTemplate, PersonProfileImage, PersonDetail, PersonCareerObjective,
                     PersonWorkExperience, PersonAcademicQualification, PersonCertificationCourse, PersonProject,
                     PersonPosition, PersonSkill, PersonHobbie, PersonKnownLanguage)
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django_tex.shortcuts import render_to_pdf
from .tex import render_pdf, tex_to_pdf, render_tex
User = get_user_model()


def home(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            messages.success(request, "Welcome back")
            return redirect('dashboard')
        else:
            messages.success(request, "Dont mess with the system")
            return redirect("logout")
    return render(request, 'builder/index.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None and password is None:
            messages.error(request, 'Invalid email or password')
            return redirect('signup')
        else:
            msg_p = passvalid(password)
            msg_e = isEmailAddressValid(email)
            if msg_p == "Valid" and msg_e == "Valid":
                if User.objects.filter(email=email).count() == 0:
                    newuser = User.objects.create_user(email=email, password=password)
                    newuser.save()
                    user = authenticate(request, email=email, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'User succesfully registered')
                        return redirect('careerobjectiveform')
                else:
                    messages.info(request, "Email already exist")
                    return redirect('signup')
            else:
                messages.error(request, 'Check your email and password. Password length '
                                        'have to be 8 or more. User must contain Alphabets and Numbers. ')
                return redirect('signup')
    return render(request, 'builder/signup.html')


def loginuser(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            messages.success(request, "Already loggedin on other page")
            return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is not None and password is not None:
            msg_e = isEmailAddressValid(email)
            if msg_e == 'Valid':
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'User succesfully loggedin')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid email or password')
                    return redirect('login')
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    return render(request, 'builder/login.html')


def logoutuser(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            logout(request)
            messages.success(request, "Successfully logged out")
            return redirect('login')
    return redirect('home')

@login_required()
def dashboard(request):
    current_user = request.user
    email = current_user.email
    user_sid = current_user.user_sid
    user_cid = current_user.user_cid
    validation_on_submit = uservalidator(email, user_sid, user_cid)
    if validation_on_submit == "Valid":
        templates = ResumeTemplate.objects.filter(resume_type="Free")
        templatespremium = ResumeTemplate.objects.filter(resume_type="Premium")
        profile = PersonProfileImage.objects.filter(person=current_user).first()
        context = {'templates': templates, 'ptemplates': templatespremium, 'profile': profile}
        messages.success(request, "Currently no need to upgrade you can use any resume template.")
        return render(request, 'builder/dashboard.html', context)
    return redirect('login')

@login_required()
def resumetemplate(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            data = request.POST
            images = request.FILES.getlist('image')
            print(images)
            if data['type'] != 'none':
                typeo = Type.objects.get(id=data['type'])
                typer = typeo.type

            for image in images:
                ResumeTemplate.objects.create(
                    resume_type=typer,
                    resume_name=data['title'],
                    resume_image=image,
                )
                print(image)
            return redirect('resume')
    else:
        messages.error(request, "You are not superuser")
        return redirect('logout')
    type = Type.objects.all()
    context = {'types': type}
    return render(request, 'builder/templateadmin.html', context)


@login_required()
def typeadd(request):
    if request.user.is_superuser:
        if request.method == "POST":
            type = request.POST.get('type')
            Type.objects.create(
                type=type
            )
            return redirect('type')
    return render(request, 'builder/type.html')


@login_required()
def personaldetails(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            profile = PersonProfileImage.objects.filter(person=current_user).first()
            objective = PersonCareerObjective.objects.filter(person=current_user).first()
            details = PersonDetail.objects.filter(person=current_user).first()
            context = {'profile': profile, 'details': details, 'objective': objective}
            return render(request, 'builder/personaldetails.html', context)
        else:
            return HttpResponse(memoryview(b'unverified.'))
    return HttpResponse(memoryview(b'unverified.'))


@login_required()
def academic(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            profile = PersonProfileImage.objects.filter(person=current_user).first()
            academic = PersonAcademicQualification.objects.filter(person=current_user)
            certificate = PersonCertificationCourse.objects.filter(person=current_user)
            context = {'profile': profile, 'academic': academic, 'certificate': certificate}
            return render(request, 'builder/education.html', context)
        else:
            return HttpResponse(memoryview(b'unverified.'))
    return HttpResponse(memoryview(b'unverified.'))


@login_required()
def workex(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            works = PersonWorkExperience.objects.filter(person=current_user)
            projects = PersonProject.objects.filter(person=current_user)
            profile = PersonProfileImage.objects.filter(person=current_user).first()
            context = {'profile': profile, 'works': works, 'projects': projects}
            return render(request, 'builder/experience.html', context)
        else:
            return HttpResponse(memoryview(b'unverified.'))
    return HttpResponse(memoryview(b'unverified.'))


@login_required()
def extra(request):
    print(request.META['REMOTE_ADDR'])
    if request.user.is_authenticated:

        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            profile = PersonProfileImage.objects.filter(person=current_user).first()
            positions = PersonPosition.objects.filter(person=current_user)
            context = {'profile': profile, 'positions': positions}
            return render(request, 'builder/extra.html', context)
        else:
            return HttpResponse(memoryview(b'unverified.'))
    return HttpResponse(memoryview(b'unverified.'))

@login_required()
def personalform(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                image = request.FILES.get('image')
                uname = request.POST.get('name')
                ucontact = request.POST.get('contact')
                uaddress = request.POST.get('address')
                uemail = request.POST.get('email')
                uprofile = request.POST.get('profile')
                if len(ucontact) != 10:
                    messages.info(request, f'Your contact length is {len(pcontact)} and contact number '
                                           f'length should be 10 digit.')
                    return redirect('workexperienceform')
                else:
                    PersonDetail.objects.create(name=uname, email=uemail, address=uaddress, contact=ucontact,
                                                   profile=uprofile, person=current_user)
                    PersonProfileImage.objects.create(image=image, person=current_user)
                    messages.success(request, "Personal Details has been saved.")
                    return redirect('personaldetailsform')
            return render(request, 'builder/personaldetailform.html')

@login_required()
def careerobjective(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                aim = request.POST.get('aim')
                if aim == " " or aim == None:
                    messages.error(request, "Please check your content")
                    return redirect('personaldetailsform')
                else:
                    PersonCareerObjective.objects.create(aim=aim, person=current_user)
                    messages.success(request, "Career objective/aim has been saved")
            return render(request, 'builder/objectivename.html')

@login_required()
def workexperience(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                name = request.POST.get('name')
                position = request.POST.get('position')
                duration1 = request.POST.get('duration1')
                duration2 = request.POST.get('duration2')
                city = request.POST.get('city')
                details = request.POST.get('workdetails')
                if name == " " or name == None:
                    messages.error(request, "Please check your company name")
                    return redirect('workexperienceform')
                if position == " " or position == None:
                    messages.error(request, "Please check your position content")
                    return redirect('workexperienceform')
                if city == " " or city == None:
                    messages.error(request, "Please check your city content")
                    return redirect('workexperienceform')
                if details == " " or details == None:
                    messages.error(request, "Please check your details content")
                    return redirect('workexperienceform')
                duration = f'''{duration1} to {duration2}'''
                PersonWorkExperience.objects.create(name=name, position=position, duration=duration, city=city,
                                                     details=details, person=current_user)
                messages.success(request, f'''Your work experience for the company: {name} has been saved. 
                Press next if you don't have more companies to add''')
                return redirect('workexperienceform')
            return render(request, 'builder/workexperienceform.html')

@login_required()
def academicqualification(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                qualification = request.POST.get('qualification')
                institution = request.POST.get('institution')
                passed = request.POST.get('year')
                city = request.POST.get('city')
                if qualification == " " or qualification == None:
                    messages.error(request, "Please check your qualification name")
                    return redirect('academicqualificationfrom')
                if institution == " " or institution == None:
                    messages.error(request, "Please check your institution content")
                    return redirect('academicqualificationfrom')
                if city == " " or city == None:
                    messages.error(request, "Please check your city content")
                    return redirect('academicqualificationfrom')
                if passed == " " or passed == None:
                    messages.error(request, "Please check your content")
                    return redirect('academicqualificationfrom')
                PersonAcademicQualification.objects.create(qualification=qualification, institution=institution,
                                                           passed=passed, city=city, person=current_user)
                messages.success(request, f'''Your qualification for '{qualification}' has been saved. 
                Press next if you don't have more to add in qualifications.''')
                return redirect('academicqualificationfrom')
            return render(request, 'builder/academicform.html')

@login_required()
def certificatecourses(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                name = request.POST.get('name')
                institution = request.POST.get('institution')
                year = request.POST.get('year')
                details = request.POST.get('details')
                if name == " " or name == None:
                    messages.error(request, "Please check your content")
                    return redirect('certificatecoursesform')
                if institution == " " or institution == None:
                    messages.error(request, "Please check your content")
                    return redirect('certificatecoursesform')
                if year == " " or year == None:
                    messages.error(request, "Please check your content")
                    return redirect('certificatecoursesform')
                if details == " " or details == None:
                    messages.error(request, "Please check your content")
                    return redirect('certificatecoursesform')
                PersonCertificationCourse.objects.create(name=name, institution=institution,
                                                         year=year, details=details, person=current_user)
                messages.success(request, f'''Your certificstion for '{name}' has been saved. 
                Press next if you don't have more to add in certificate courses.''')
                return redirect('certificatecoursesform')
            return render(request, 'builder/certificationsform.html')

@login_required()
def projects(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                name = request.POST.get('name')
                details = request.POST.get('details')
                if name == " " or name == None:
                    messages.error(request, "Please check your content")
                    return redirect('projectsform')
                if details == " " or details == None:
                    messages.error(request, "Please check your content")
                    return redirect('projectsform')
                PersonProject.objects.create(name=name, details=details, person=current_user)
                messages.success(request, f'''Your project '{name}' has been saved. 
                Press next if you don't have more to add in projects section.''')
                return redirect('projectsform')
            return render(request, 'builder/projectsform.html')

@login_required()
def positionsres(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                name = request.POST.get('name')
                place = request.POST.get('place')
                year = request.POST.get('year')
                details = request.POST.get('details')
                if name == " " or name == None:
                    messages.error(request, "Please check your content")
                    return redirect('positionsresform')
                if place == " " or place == None:
                    messages.error(request, "Please check your content")
                    return redirect('positionsresform')
                if year == " " or year == None:
                    messages.error(request, "Please check your content")
                    return redirect('positionsresform')
                if details == " " or details == None:
                    messages.error(request, "Please check your content")
                    return redirect('positionsresform')
                PersonPosition.objects.create(name=name, place=place, year=year, details=details, person=current_user)
                messages.success(request, f'''Your position '{name}' has been saved. 
                Press next if you don't have more to add in position section.''')
                return redirect('positionsresform')
            return render(request, 'builder/positionform.html')

@login_required()
def skillsets(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                skill = request.POST.get('skill')
                if skill == " " or skill == None:
                    messages.error(request, "Please check your content")
                    return redirect('skillsetsform')
                PersonSkill.objects.create(skill=skill, person=current_user)
                messages.success(request, f'''Your skill: '{skill}' has been saved. 
                Press next if you don't have more to add in skill section.''')
                return redirect('skillsetsform')
            return render(request, 'builder/skillform.html')

@login_required()
def hobbies(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                hobby = request.POST.get('hobby')
                if hobby == " " or hobby == None:
                    messages.error(request, "Please check your content")
                    return redirect('hobbiesform')
                PersonHobbie.objects.create(hobby=hobby, person=current_user)
                messages.success(request, f'''Your hobby: '{hobby}' has been saved. 
                Press next if you don't have more to add in hobby section.''')
                return redirect('hobbiesform')
            return render(request, 'builder/interestsform.html')

@login_required()
def knownlanguage(request):
    if request.user.is_authenticated:
        current_user = request.user
        email = current_user.email
        user_sid = current_user.user_sid
        user_cid = current_user.user_cid
        validation_on_submit = uservalidator(email, user_sid, user_cid)
        if validation_on_submit == "Valid":
            if request.method == "POST":
                lang = request.POST.get('lang')
                if lang == " " or lang == None:
                    messages.error(request, "Please check your content")
                    return redirect('knownlanguageform')
                PersonKnownLanguage.objects.create(lang=lang, person=current_user)
                messages.success(request, f'''Your language: '{lang}' has been saved. 
                Press next if you don't have more to add in language section.''')
                return redirect('knownlanguageform')
            return render(request, 'builder/languagesform.html')

def render_to_pdfe(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            current_user = request.user
            email = current_user.email
            user_sid = current_user.user_sid
            user_cid = current_user.user_cid
            validation_on_submit = uservalidator(email, user_sid, user_cid)
            if validation_on_submit == "Valid":
                person = PersonDetail.objects.filter(person=current_user).first()
                objective = PersonCareerObjective.objects.filter(person=current_user).first()
                works = PersonWorkExperience.objects.filter(person=current_user)
                projects = PersonProject.objects.filter(person=current_user)
                educations = PersonAcademicQualification.objects.filter(person=current_user)
                certificates = PersonCertificationCourse.objects.filter(person=current_user)
                skills = PersonSkill.objects.filter(person=current_user)
                languages = PersonKnownLanguage.objects.filter(person=current_user)
                interests = PersonHobbie.objects.filter(person=current_user)
                positions = PersonPosition.objects.filter(person=current_user)
                data = {'person': person, 'objective': objective, 'works': works,
                        'projects': projects, 'educations': educations, 'certificates': certificates,
                        'skills': skills, 'languages': languages, 'interests': interests, 'positions': positions
                        }
                pdf = render_to_pdfe('builder/resumepdfgen.html', data)
                return HttpResponse(pdf, content_type='application/pdf')

def texview(request):
    template_name = 'builder/test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')


def test123(request):
    template = 'builder/test.tex'
    context = {'foo': 'Bar'}
    tex_file = render_tex(request, template, context)
    tex_cmd = 'pdflatex'
    flags = ('-interaction=nonstopmode', '-halt-on-error')
    do_link_imgs = True
    return tex_to_pdf(tex_file, tex_cmd=tex_cmd, flags=flags, do_link_imgs=do_link_imgs)
    '''template_name = 'builder/test.tex'
    context = {'foo': 'Bar'}
    return render_pdf(request, template_name, context, filename='checkmate.pdf')'''
