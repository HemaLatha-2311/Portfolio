
import os
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
def home(request):
    return render (request,"home.html")

def about(request):
    return render (request,"about.html")

def projects(request):
    project_list = [
        {
            'title': 'Multivendor Marketplace',
            'tech_stack': 'Python, SQLite3, OOP',
            'description': 'Developed a marketplace system where multiple vendors can register securely and manage their own products. Key features include secure login, product CRUD operations, and a user-friendly interface built using Python and SQLite3.',
            'image': 'images/multivendor.png'  # Add this image in your static folder
        },
        {
            'title': 'ATM System Using Fingerprint',
            'tech_stack': 'Biometric Module, Embedded Systems',
            'description': 'Designed a fingerprint-based ATM system as a secure replacement for physical ATM cards. The system uses biometric authentication to ensure that only authorized users can access ATM functionalities.',
            'image': 'images/atm.PNG'  # Add this image in your static folder
        },
    ]
    return render(request, "projects.html", {'projects': project_list})



def experience(request):
    experience = [
        {
            "company": "WiseLearnz",
            "position": "Python Full Stack Developer Trainee",
            "logo": "images/wiselearnz.jpg",
            "points": [
                "Completed Training and Internship Program (TIP) with an impressive Grade A(83%)",
                "Executed 4 OOPS Projects showcasing strong object-orieted programming skills.",
                "Developed 2 Tkinter applications demonstrating proficiency in graphical user interface development."
            ]
        },
        {
            "company": "Sparky Entertainment Private Limited",
            "position": "Junior Python Developer",
            "logo": "images/sparky.png",
            "points": [
                "Commitment to delivering superior quality animation that exceeds industry standards.",
                "Utilied Python, MEL(Maya Embedded Language) and designed tool's user interfaces using PYQT5 and Qt.",
                "Designer to create user-friendly and efficient animation tools."
            ]
        }
    ]

    return render (request,"experience.html", {"experience" : experience})     

def certification (request):

    return render (request,"certification.html")   



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],  # 👈 Your email address
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully!")
        
    return render(request, "contact.html")


def resume(request):
    resume_path = finders.find("myapp/resume.pdf")
    if resume_path:
        with open(resume_path, "rb") as resume_file:
            response = HttpResponse(resume_file.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            return response
    else:
        return HttpResponse("Resume Not Found", status=404)

