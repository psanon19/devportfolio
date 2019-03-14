from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('skills/', views.wildCards, name='wildCard'),
    path('resume/', views.resume, name='oneTwo'),
    path('showcase/', views.showcase, name='showcase'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('contact/', views.contact_me, name='contact'),
]