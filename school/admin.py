from django.contrib import admin
from .models import Student, AcademicYear, Discipline, Classroom


admin.site.register(Student)
admin.site.register(AcademicYear)
admin.site.register(Discipline)
admin.site.register(Classroom)
