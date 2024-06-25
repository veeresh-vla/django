from django.urls import path
from .import views
urlpatterns=[
    path('exams/',views.exams_view),
    path('attendence/',views.attendance_view),
    path('fees/',views.fees_view),
]