from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.chatbot,
        name='chatbot'
    ),


    path(
        'syllabus/<str:specialization>/',
        views.syllabus_view,
        name='syllabus'
    ),

]