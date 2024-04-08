# Generated by Django 5.0.3 on 2024-04-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_project_roles_alter_project_industry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='acquired_skills',
        ),
        migrations.RemoveField(
            model_name='project',
            name='industry',
        ),
        migrations.AddField(
            model_name='project',
            name='result',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='school',
            field=models.CharField(choices=[('ИШИТР', 'ИШИТР'), ('ИШПР', 'ИШПР'), ('ИШЭ', 'ИШЭ'), ('ИШЯТ', 'ИШЯТ'), ('ИШНКБ', 'ИШНКБ'), ('ИШНПТ', 'ИШНПТ'), ('БШ', 'БШ')], default='ИШИТР', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('УИРС', 'УИРС'), ('НИРС', 'НИРС'), ('ВКР', 'ВКР')], default='УИРС', max_length=50),
        ),
        migrations.DeleteModel(
            name='AcquiredSkill',
        ),
    ]
