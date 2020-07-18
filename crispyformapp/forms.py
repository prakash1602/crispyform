from django import forms
from .models import StudentDetails


class StudentDataForm(forms.ModelForm):
    class Meta:
        model = StudentDetails

        fields = ['first_name', 'last_name', 'email', 'mobile', 'marks', 'fee', 'college', 'course', 'branch', 'location',
              'institute']

    def __init__(self, *args, **kwargs):
        super(StudentDataForm, self).__init__(*args, **kwargs)
        self.fields['branch'].empty_label = 'Select'
        self.fields['course'].empty_label = 'Select'
        self.fields['location'].empty_label = 'Select'
        self.fields['college'].empty_label = 'Select'
        self.fields['institute'].empty_label = 'Select'
