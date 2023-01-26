from rest_framework import viewsets
from school.api import serializers
#from school import models
from school.models import Student, AcademicYear, Discipline, Classroom

class StudentViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSrializer
    queryset = Student.objects.all()

class AcademicYearViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.AcademicYearSrializer
    queryset = AcademicYear.objects.all()

class DisciplineViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.DisciplineSrializer
    queryset = Discipline.objects.all()

class ClassroomViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ClassroomSrializer
    queryset = Classroom.objects.all()
