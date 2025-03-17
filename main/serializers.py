from rest_framework.serializers import ModelSerializer
from .models import *


class MentorSerializer(ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
