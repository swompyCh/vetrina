from .models import Student, Project, ProjectRole, Requirement, Vacancy, CVStudent, UserRole, \
    StudentParticipation, Lecturer, LogActivity #AcquiredSkill
from django.forms import ModelForm, TextInput, DateInput, Textarea, Select
from django import forms


class ProjectForm(ModelForm):
    # requirements = forms.CharField(widget=forms.Textarea, required=False)
    # acquired_skills = forms.CharField(widget=forms.Textarea, required=False)
    roles = forms.ModelMultipleChoiceField(queryset=ProjectRole.objects.all(), required=True)

    class Meta:
        model = Project
        fields = ['title', 'goal', 'description', 'created_date', 'start_date', 'date_prototype', 'end_date',
                  'type', 'status', 'tasks', 'result', 'school']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта'
            }),
            "goal": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цель проекта'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание проекта'
            }),
            "created_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата создания проекта'

            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата начала работы над проектом'

            }),
            "date_prototype": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата защиты прототипа'

            }),
            "end_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата завершения проекта'

            }),
            "type": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип проекта'
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Статус проекта'
            }),
            "tasks": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача проекта'
            }),
            "result": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Результат проекта'
            }),
            "school": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Школа'
            }),

        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['roles'].widget.attrs.update({'class': 'form-control'})
            # self.fields['acquired_skills'].widget.attrs.update({'placeholder': 'Enter acquired skills, one per line'})


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = ['role', 'description']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['role', 'requirements']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'requirements': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class UpdateProjectAndRequirementsForm(forms.ModelForm):
    role_choices = [(1, 'Backend'), (2, 'Frontend'), (3, 'Web'), (4, 'Тестировщик')]  # Пример выбора ролей

    roles = forms.MultipleChoiceField(choices=role_choices, widget=forms.CheckboxSelectMultiple, label='Roles')
    description = forms.CharField(widget=forms.Textarea, label='Description')

    class Meta:
        model = Project
        fields = ['title', 'goal', 'description', 'start_date', 'date_prototype', 'end_date', 'type', 'status', 'tasks',
                  'result', 'school']
