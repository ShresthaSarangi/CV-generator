from .models import Profile
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Create your views here.
def dashboard(request):
    resumes = Profile.objects.all()
    return render(request,'myapp/modern-dashboard.html',{'resumes':resumes})

def save_profile(request):
    if request.method=="POST":
        # Step1: Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        summary = request.POST.get('summary')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        # Step 2: Save data into database
        profile = Profile(name=name,email=email,phone=phone,degree=degree,school=school,university=university,summary=summary,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('dashboard')
    return render(request,'myapp/modern_create_profile.html')

def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,'myapp/modern-resume.html',{'user_profile':user_profile})


def download_resume(request,id):
    user_profile = get_object_or_404(Profile,id=id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user_profile.name}_CV.pdf"'

    p = canvas.Canvas(response)

    y = 800

    p.setFont("Helvetica-Bold", 22)
    p.drawString(50, y, user_profile.name)

    y -= 25
    p.setFont("Helvetica", 12)
    p.drawString(50, y, f"Email: {user_profile.email}")
    y -= 20
    p.drawString(50, y, f"Phone: {user_profile.phone}")

    y -= 40
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Education")

    y -= 20
    p.setFont("Helvetica", 12)
    p.drawString(60, y, f"Degree: {user_profile.degree}")
    y -= 20
    p.drawString(60, y, f"School: {user_profile.school}")
    y -= 20
    p.drawString(60, y, f"University: {user_profile.university}")

    y -= 40
    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Professional Summary")

    y -= 20
    p.setFont("Helvetica", 12)
    text = p.beginText(60, y)
    for line in user_profile.summary.split('\n'):
        text.textLine(line)
    p.drawText(text)

    y = text.getY() - 20

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Work Experience")

    y -= 20
    p.setFont("Helvetica", 12)
    text = p.beginText(60, y)
    for line in user_profile.previous_work.split('\n'):
        text.textLine(line)
    p.drawText(text)

    y = text.getY() - 20

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, y, "Skills")

    y -= 20
    p.setFont("Helvetica", 12)
    text = p.beginText(60, y)
    for line in user_profile.skills.split(','):
        text.textLine(f"• {line.strip()}")
    p.drawText(text)

    p.showPage()
    p.save()

    return response

def delete(request, id):
    profile = get_object_or_404(Profile,id=id)
    profile.delete()
    return redirect('dashboard')

def edit(request, id):
    profile = get_object_or_404(Profile, id=id)

    if request.method == "POST":
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.degree = request.POST.get('degree')
        profile.school = request.POST.get('school')
        profile.university = request.POST.get('university')
        profile.summary = request.POST.get('summary')
        profile.previous_work = request.POST.get('previous_work')
        profile.skills = request.POST.get('skills')

        profile.save()
        return redirect('dashboard')

    return render(request, 'myapp/edit.html', {'profile': profile})