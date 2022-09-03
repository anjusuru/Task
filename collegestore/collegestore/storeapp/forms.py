from django import forms
from .models import Order,Course,Department


class OrderForm(forms.ModelForm):
    MATERIALS_CHOICES = (
        ("1", "debit notebook"),
        ("2", "pen"),
        ("3", "exam papers"),
        ("4", "stapler"),
    )
    materials_provided=forms.MultipleChoiceField(choices=MATERIALS_CHOICES,widget=forms.CheckboxSelectMultiple)

    def clean_my_field(self):
        if len(self.cleaned_data['materials_provided']) > 3:
            raise forms.ValidationError('Select no more than 3.')
        return self.cleaned_data['materials_provided']

    class Meta:
        model = Order
        fields = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course',
                  'purpose', 'materials_provided')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()
        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
