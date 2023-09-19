from django.contrib import admin
from myapp1.models import Student,Faculty,Attendance,Leave

# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Attendance)
admin.site.register(Leave)

