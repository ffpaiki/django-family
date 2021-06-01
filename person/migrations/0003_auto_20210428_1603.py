# Generated by Django 3.2 on 2021-04-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_place_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='firstname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='place_of_birth',
            field=models.TextField(),
        ),
    ]
