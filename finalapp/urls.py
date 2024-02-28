from django.urls import path

from . import views

urlpatterns = [
    path('home' , views.home , name='home'),
    path("", views.index, name="index"),
    path('createClassroom' , views.createClassroom, name="createClassroom"),
    path('room/<int:room_id>' , views.room , name="room"),
    path("addStudent", views.addStudent, name="addStudent"),
    path('editStudent/<int:Student_id>' , views.editStudent, name="editStudent"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('upload_csv', views.upload_csv , name="upload_csv"),
    path('deleteStudent/' , views.deleteStudent , name="deleteStudent"),
    path('deleteRoom/<int:room_id>' , views.deleteRoom , name='deleteRoom'),
    path('error' , views.error , name="error"),
]
