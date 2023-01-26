# Django-Rest-API
 APIs for school management system built with django and django rest framework

### Requirements
 Python 3.9.2

### Installation
 pip install -r requirements.txt

## Migrations
 python manage.py makemigrations
 python manage.py migrate 

### Run roject
 python manage.py runserver

### Json document example
# Student
 ```JSON
{
    "studentName": "Mary",
    "registration": "123"
},
```
# Academic Year
 ```JSON
{
    "academicYearName": "2023",
},
```
# Discipline
 ```JSON
{
    "disciplineName": "math"
},
```
# Classroom
 ```JSON
{
    "schoolGrade": "1",
    "schoolClass": "a",
    "academicYear": 1,
    "discipline": [
        1,
        2,
        3
    ],
    "student": [
        1,
        2
    ]
}
```
