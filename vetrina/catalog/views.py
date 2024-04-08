from django.db import transaction
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import ProjectForm, RequirementForm, VacancyForm, UpdateProjectAndRequirementsForm
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from .models import Student, Project, ProjectRole, Requirement, Vacancy, CVStudent, UserRole, \
    StudentParticipation, Lecturer, LogActivity  # AcquiredSkill
from django.http import HttpResponseRedirect

# RequirementFormSet = inlineformset_factory(Project, Requirement, fields=('role', 'description'), extra=1)
# AcquiredSkillFormSet = inlineformset_factory(Project, AcquiredSkill, fields=('role', 'description'), extra=1)
VacancyFormSet = inlineformset_factory(Project, Vacancy, form=VacancyForm, extra=1)  # 'acquired_skills'
RequirementFormSet = inlineformset_factory(Project, Requirement, form=RequirementForm, extra=1)


def catalog(request):
    projects = Project.objects.all()

    for project in projects:
        vacancies = Vacancy.objects.filter(project=project)
        project.vacancies.set(vacancies)

    return render(request, 'catalog/index.html', {'projects': projects})


class CatalogDetailView(DetailView):
    model = Project
    template_name = 'catalog/details_view.html'
    context_object_name = 'project'

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'requirements',
            'requirements__role',
            # 'acquired_skills',
            # 'acquired_skills__role',
            'vacancies',
            'vacancies__role',
            'vacancies__requirements',
            # 'vacancies__acquired_skills',
        )


class CatalogUpdateView(UpdateView):
    success_url = '/catalog/'
    model = Project
    template_name = 'catalog/catalog-update.html'
    fields = ['title', 'goal', 'description', 'created_date', 'start_date', 'date_prototype', 'end_date',
              'type', 'status', 'tasks', 'result', 'school', 'roles']

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()

        # Update or create Requirement instances from dynamic fields
        roles = form.cleaned_data['roles']
        for role in roles:
            requirements_key = f"requirements_{role.title.lower().replace(' ', '_')}"
            requirement_data = self.request.POST.get(requirements_key, '').splitlines()
            for req_desc in requirement_data:
                requirement, created = Requirement.objects.update_or_create(project=project, role=role, defaults={'description': req_desc})
                if not created:
                    requirement.description = req_desc
                    requirement.save()

        # Update or create Vacancy instances
        existing_roles = set(project.roles.all())
        for role in roles:
            requirement = Requirement.objects.filter(project=project, role=role).first()
            vacancy, created = Vacancy.objects.update_or_create(project=project, role=role, defaults={'requirements': requirement})
            if not created:
                vacancy.requirements = requirement
                vacancy.save()
            existing_roles.discard(role)

        # Delete Vacancy instances for unselected roles
        for role in existing_roles:
            Vacancy.objects.filter(project=project, role=role).delete()

        return super().form_valid(form)


class CatalogDeleteView(DeleteView):
    model = Project
    success_url = '/catalog/'
    template_name = 'catalog/catalog-delete.html'


def create(request):
    error = ''
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            project.roles.set(form.cleaned_data['roles'])

            # Create Requirement instances from dynamic fields
            roles = form.cleaned_data['roles']
            for role in roles:
                requirements_key = f"requirements_{role.title.lower().replace(' ', '_')}"
                requirement_data = request.POST.get(requirements_key, '').splitlines()
                for req_desc in requirement_data:
                    Requirement.objects.create(project=project, role=role, description=req_desc)

            # Create Vacancy instances
            for role in roles:
                requirement = Requirement.objects.filter(project=project, role=role).first()
                Vacancy.objects.create(project=project, role=role, requirements=requirement)

            return redirect('home')
        else:
            error = 'Form was invalid'

    form = ProjectForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'catalog/create.html', data)
