from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_list, name='member-list'),
    path('nieuw/', views.member_create, name='member-create'),
    path('succes/', views.member_success, name='member-success'),
]
