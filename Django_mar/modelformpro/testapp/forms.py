from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Student
        fields = '__all__'
