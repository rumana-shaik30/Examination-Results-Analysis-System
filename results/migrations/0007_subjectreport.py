# Generated by Django 3.1.1 on 2020-10-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjectreport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnterName', models.CharField(max_length=15)),
                ('Rollno', models.IntegerField(null=True)),
                ('SelectDepartment', models.CharField(max_length=15)),
                ('SelectSemester', models.IntegerField(null=True)),
            ],
        ),
    ]