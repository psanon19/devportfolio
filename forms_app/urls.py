from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('wildcard/', views.wildCards, name='wildCard'),
    path('resume/', views.resume, name='resume'),
    path('showcase/', views.showcase, name='showcase'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('contact/', views.contact_me, name='contact'),
    path('reflections/', views.reflections, name='relections'),
]