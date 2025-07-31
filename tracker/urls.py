from django.urls import path
from .views import bug_list, bug_detail, bug_create, edit_bug   

urlpatterns = [
    path('', bug_list, name='bug_list'),
    path('bug/<int:pk>/', bug_detail, name='bug_detail'),
    path('create/', bug_create, name='bug_create'),
    path('bug/<int:pk>/edit/',edit_bug, name='edit_bug'),  
]