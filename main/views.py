from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, CreateAPIView,
    RetrieveAPIView, DestroyAPIView,
    UpdateAPIView, RetrieveUpdateAPIView,
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
)
from .serializers import *


class MentorListCreateAPIView(ListCreateAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()


class MentorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()


class GroupListCreateAPIView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class GroupRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class StudentListCreateAPIView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class PaymentListCreateAPIView(ListCreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
