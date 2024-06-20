from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from django.urls import reverse

from .models import Task, Tag

class TaskForm(forms.ModelForm):
    priority = forms.ChoiceField(label='Prioridade', choices=Task.PRIORITY_CHOICES, required=True)
    tags = forms.CharField(max_length=200, required=False, help_text='Separe as tags por vírgula', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'tags', 'priority', 'due_date']
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
            Field('tags', css_class='form-control'),
            Field('priority', css_class='form-control'),
            Field('due_date', css_class='form-control'),
            Submit('submit', 'Salvar', css_class='btn btn-primary'),
            HTML('<a class="btn btn-secondary" href="%s">Cancelar</a>' % reverse('list_task')),

        )
        if self.instance.pk:
            tags = ','.join(tag.name for tag in self.instance.tags.all())
            self.initial['tags'] = tags
