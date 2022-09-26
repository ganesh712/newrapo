from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
     path('studentapi/', views.Student_API.as_view()),
     path('studentapi/<int:pk>', views.Student_API.as_view()),
]
