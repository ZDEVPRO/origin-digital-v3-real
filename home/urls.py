from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects_view, name='projects'),
    # path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
