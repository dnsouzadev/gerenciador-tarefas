from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

from .models import Task, Project, Tag

class TaskForm(forms.ModelForm):
    priority = forms.ChoiceField(label='Prioridade', choices=Task.PRIORITY_CHOICES, required=True)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), label='Projeto', required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), label='Tags', required=False, widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'tags', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('description', css_class='form-control'),
            Field('project', css_class='form-control'),
            Field('tags', css_class='form-control'),
            Field('priority', css_class='form-control'),
            Field('due_date', css_class='form-control'),
            Submit('submit', 'Salvar', css_class='btn btn-primary'),
        )
