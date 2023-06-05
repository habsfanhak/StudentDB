# Generated by Django 4.1.7 on 2023-06-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
