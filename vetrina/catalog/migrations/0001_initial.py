# Generated by Django 5.0.3 on 2024-04-01 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ID_project', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('goal', models.TextField()),
                ('description', models.TextField()),
                ('created_date', models.DateField()),
                ('start_date', models.DateField()),
                ('date_prototype', models.DateField()),
                ('end_date', models.DateField()),
                ('industry', models.CharField(choices=[('EdTech', 'EdTech'), ('MedTech', 'MedTech')], max_length=50)),
                ('status', models.CharField(choices=[('active', 'Активен'), ('completed', 'Завершен'), ('team_forming', 'Формирование команды')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('facultet', models.CharField(max_length=100)),
                ('group_number', models.CharField(max_length=20)),
                ('photo', models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AcquiredSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acquired_skills', to='catalog.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acquired_skills', to='catalog.projectrole')),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='catalog.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='catalog.projectrole')),
            ],
        ),
        migrations.CreateModel(
            name='LogActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_action', models.DateField()),
                ('time_action', models.TimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='catalog.student')),
            ],
        ),
        migrations.CreateModel(
            name='CVStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_grade', models.DecimalField(decimal_places=2, max_digits=3)),
                ('summary', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cvs', to='catalog.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='catalog.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='catalog.projectrole')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to='catalog.student')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquired_skills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='catalog.acquiredskill')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='catalog.project')),
                ('requirements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='catalog.requirement')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='catalog.projectrole')),
            ],
        ),
    ]