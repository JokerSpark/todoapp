from django import forms
from todoapp.models import task


class create_task(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'