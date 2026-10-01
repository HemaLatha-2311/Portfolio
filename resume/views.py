
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
            'title': 'Customer Churn Prediction',
            'tech_stack': 'Python, Pandas, scikit-learn, Matplotlib',
            'description': 'Built an end-to-end machine learning pipeline to predict customer churn. Performed data preprocessing, feature engineering, model training, comparison, and evaluation to identify customers at risk of leaving.',
            'image': 'images/churn_prediction.png'
        },
        {
            'title': 'Support Ticket Text Classifier',
            'tech_stack': 'Python, scikit-learn, NLTK, FastAPI',
            'description': 'Developed an NLP-based text classification system to categorize support tickets automatically. Built a FastAPI endpoint to expose the trained classification model for application use.',
            'image': 'images/support_ticket.png'
        },
        {
            'title': 'Task Management API',
            'tech_stack': 'Python, FastAPI, PostgreSQL, REST API',
            'description': 'Developed a REST API for task management with CRUD operations and task assignment functionality. Used FastAPI for API development and PostgreSQL for database management.',
            'image': 'images/task_management.png'
        },
        {
            'title': 'AWS File Upload & Management',
            'tech_stack': 'Python, AWS EC2, AWS S3, REST API',
            'description': 'Developed a file management application for secure file upload, storage, retrieval, and deletion. Integrated AWS S3 for cloud storage and AWS EC2 for application deployment.',
            'image': 'images/aws_file_management.png'
        },
        {
            'title': 'Multi-Region Tool Sync',
            'tech_stack': 'Python, REST API, MySQL, Microsoft Teams API',
            'description': 'Developed a synchronization system for internal tools across India, Malaysia, and Singapore. Integrated REST APIs and MySQL for data synchronization and Microsoft Teams API for notifications.',
            'image': 'images/multi_region_sync.png'
        },
        {
            'title': 'Multivendor Marketplace',
            'tech_stack': 'Python, SQLite, REST API',
            'description': 'Developed a multivendor marketplace application with vendor authentication, product management, CRUD operations, and vendor-specific access to products.',
            'image': 'images/multivendor.png'
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

        full_message = (
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n\n"
            f"Message:\n{message}"
        )

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            messages.success(
                request,
                "Your message has been sent successfully!"
            )

        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(
                request,
                "Sorry, your message could not be sent. Please try again."
            )

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

