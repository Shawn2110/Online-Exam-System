# Generated by Django 3.1.14 on 2024-03-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0004_auto_20240309_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_registration',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant_registration',
            name='phone',
            field=models.CharField(default='234', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='applicant_registration',
            name='reg_No',
            field=models.CharField(default='23u764', max_length=20, unique=True),
        ),
    ]
