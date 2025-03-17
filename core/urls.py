from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentors/', MentorListCreateAPIView.as_view()),
    path('mentors/<int:pk>/', MentorRetrieveUpdateDestroyAPIView.as_view()),
    path('groups/', GroupListCreateAPIView.as_view()),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view()),
    path('students/', StudentListCreateAPIView.as_view()),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('payments/', PaymentListCreateAPIView.as_view()),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view()),
]
