# Generated by Django 3.1.1 on 2020-10-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0011_studentsreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addsubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SelectYear', models.IntegerField(null=True)),
                ('SelectSemester', models.IntegerField(null=True)),
                ('SelectDepartment', models.CharField(max_length=20)),
                ('Entersubjectcode', models.CharField(max_length=20, null=True)),
                ('Entersubjectname', models.CharField(max_length=50)),
            ],
        ),
    ]
