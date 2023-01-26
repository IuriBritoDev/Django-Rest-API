from django.urls import path, include
from school.api import viewsets 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'student', viewsets.StudentViewSets)
router.register(r'academicyear', viewsets.AcademicYearViewSets)
router.register(r'discipline', viewsets.DisciplineViewSets)
router.register(r'classroom', viewsets.ClassroomViewSets)

urlpatterns = [
    path('', include(router.urls))
]
