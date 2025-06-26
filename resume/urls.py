from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home,name="home"),
    path("about/",views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("experience/",views.experience,name="experience"),
    path("certication/",views.certification,name="certification"),
    path("contact/",views.contact,name="contact"),
    path("resume/",views.resume,name="resume")
    
]
