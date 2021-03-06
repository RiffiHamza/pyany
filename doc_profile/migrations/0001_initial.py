# Generated by Django 3.0.5 on 2020-05-11 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Speciality', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Docter Profile',
                'verbose_name_plural': 'Docters Profiles',
            },
        ),
    ]
