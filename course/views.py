
from rest_framework import generics
from rest_framework import viewsets

from .models import Course, Student, Mentor
from .serializers import CourseSerializer, StudentSerializer, MentorSerializer
from .my_generics import MyAPIView, ListMixinAPI, CreateMixinAPI, RerieveMixinAPI, UpdateMixinAPI, DeleteMixinAPI




class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class MentorCreateListViewSet(ListMixinAPI, CreateMixinAPI, viewsets.ViewSetMixin, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()


class MentorViewSet(
                    RerieveMixinAPI,
                    UpdateMixinAPI,
                    DeleteMixinAPI,
                    viewsets.ViewSetMixin,
                    MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()
