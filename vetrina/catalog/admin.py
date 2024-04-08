from django.contrib import admin
from .models import Student, Project, ProjectRole, Requirement, Vacancy, CVStudent, UserRole, StudentParticipation, Lecturer, LogActivity #AcquiredSkill


# Register your models here.
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(ProjectRole)
admin.site.register(Requirement)
# admin.site.register(AcquiredSkill)
admin.site.register(Vacancy)
admin.site.register(CVStudent)
admin.site.register(UserRole)
admin.site.register(StudentParticipation)
admin.site.register(Lecturer)
admin.site.register(LogActivity)
