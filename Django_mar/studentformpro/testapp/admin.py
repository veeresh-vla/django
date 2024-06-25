from django.contrib import admin
from testapp.forms import StudentForm
# Register your models here.

class StudentFormAdmin(admin.FormsAdmin):
    list_display=['name','rollno','marks']
admin.site.register(StudentForm,StudentFormAdmin)
