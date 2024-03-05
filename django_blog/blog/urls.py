from django.contrib import admin
from django.urls import path
from .views import blog_list, blog_details, blog_delete

urlpatterns = [
    path('', blog_list),
    path('<id>/',blog_details),
    path('<id>/delete/', blog_delete),
   
]