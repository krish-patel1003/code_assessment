# Generated by Django 3.2.5 on 2022-06-29 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api2', '0008_auto_20220625_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='question_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='code_read_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='question_read_time',
            field=models.FloatField(null=True),
        ),
    ]