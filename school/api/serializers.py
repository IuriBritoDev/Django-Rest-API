from rest_framework import serializers
#from school import models
from school.models import Student, AcademicYear, Discipline, Classroom

class StudentSrializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AcademicYearSrializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = '__all__'

class DisciplineSrializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class ClassroomSrializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'
