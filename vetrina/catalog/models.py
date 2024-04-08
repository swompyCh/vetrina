from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    facultet = models.CharField(max_length=100)
    group_number = models.CharField(max_length=20)
    photo = models.BinaryField(null=True, blank=True)


class Project(models.Model):
    ID_project = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    goal = models.TextField()
    description = models.TextField()
    created_date = models.DateField()
    start_date = models.DateField()
    date_prototype = models.DateField()
    end_date = models.DateField()
    type = models.CharField(max_length=50, choices=[('УИРС', 'УИРС'),
                                                    ('НИРС', 'НИРС'),
                                                    ('ВКР', 'ВКР')], default='УИРС')
    status = models.CharField(max_length=50, choices=[('active', 'В разработке'), ('completed', 'Завершен'),
                                                      ('team_forming', 'Формирование команды')])
    roles = models.ManyToManyField('ProjectRole', related_name='projects')
    tasks = models.TextField(default='')
    result = models.TextField(default='')
    school = models.CharField(max_length=50, choices=[('ИШИТР', 'ИШИТР'),
                                                      ('ИШПР', 'ИШПР'),
                                                      ('ИШЭ', 'ИШЭ'),
                                                      ('ИШЯТ', 'ИШЯТ'),
                                                      ('ИШНКБ', 'ИШНКБ'),
                                                      ('ИШНПТ', 'ИШНПТ'),
                                                      ('БШ', 'БШ')], default='ИШИТР')

    def __str__(self):
        return self.title


class ProjectRole(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Requirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requirements')
    role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE, related_name='requirements')
    description = models.TextField()

    def __str__(self):
        return self.description


# class AcquiredSkill(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='acquired_skills')
#     role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE, related_name='acquired_skills')
#     description = models.TextField()
#
#     def __str__(self):
#         return self.description


class Vacancy(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='vacancies')
    role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE, related_name='vacancies')
    requirements = models.ForeignKey(Requirement, on_delete=models.CASCADE, related_name='vacancies')
    # acquired_skills = models.ForeignKey(AcquiredSkill, on_delete=models.CASCADE, related_name='vacancies')


class CVStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='cvs')
    student_grade = models.DecimalField(max_digits=3, decimal_places=2)
    summary = models.TextField()


class UserRole(models.Model):
    role = models.CharField(max_length=50)


class StudentParticipation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='participations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='participations')
    role = models.ForeignKey(ProjectRole, on_delete=models.CASCADE, related_name='participations')


class Lecturer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)


class LogActivity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='logs')
    action = models.CharField(max_length=100)
    description = models.TextField()
    date_action = models.DateField()
    time_action = models.TimeField()
