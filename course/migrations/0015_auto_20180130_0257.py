# Generated by Django 2.0 on 2018-01-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_merge_20180130_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='course_code',
            field=models.CharField(max_length=10),
        ),
    ]
