from django.db import models


GRADE = (
        ('1','1'), ('2','2'), ('3','3'), ('4','4'),
    )

CLASS = (
        ('a','A'), ('b','B'), ('c','C'), ('d','D'),
    )


class Student(models.Model):
    studentName = models.CharField(max_length=255)
    registration = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.studentName}'

class AcademicYear(models.Model):
    academicYearName = models.CharField(max_length=255)
    creationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.academicYearName}'

class Discipline(models.Model):
    disciplineName = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.disciplineName}'

class Classroom(models.Model):
    schoolGrade = models.CharField(max_length=1, choices=GRADE,)
    schoolClass = models.CharField(max_length=1, choices=CLASS,)

    academicYear = models.ForeignKey(
        AcademicYear, on_delete=models.CASCADE, related_name='academicyear'
    )

    discipline = models.ManyToManyField(Discipline)
    student = models.ManyToManyField(Student)

    def __str__(self):
        return f'turma: {self.schoolGrade} - {self.schoolClass}'
