# Generated by Django 3.0.9 on 2020-08-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortApp', '0002_testcases'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sortalgorithms',
            name='sorted_result',
        ),
        migrations.RemoveField(
            model_name='sortalgorithms',
            name='unsorted_numbers',
        ),
        migrations.AddField(
            model_name='sortalgorithms',
            name='sorted_seq',
            field=models.TextField(default='', verbose_name='sorted'),
        ),
        migrations.AddField(
            model_name='sortalgorithms',
            name='unsorted_seq',
            field=models.TextField(default='', verbose_name='unsorted'),
        ),
    ]