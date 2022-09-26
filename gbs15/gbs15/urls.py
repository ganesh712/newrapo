from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    #path('studentapi/', views.Studentcreate.as_view()),
    #path('studentapi/<int:pk>', views.Studentupdate.as_view()),

    path('studentapi/', views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>', views.StudentListRetrieveUpdate.as_view()),
]

